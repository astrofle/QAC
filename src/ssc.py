#
#  taken from snippet.txt
#

"""
Last Update: 2017.09.30
- Fill free to use and modify this pipeline.
- Please consider citing the following publications
    1) https://arxiv.org/abs/1709.09365
    2) http://adsabs.harvard.edu/abs/2014A%26A...563A..99F
- Or contact Shahram Faridani (shahram.faridani@gmail.com)
**********************************
"""
import math
import os
import sys
import datetime

testMode = False

# Helper Functions

# BUNIT from the header
def getBunit(imName):
    ia.open(str(imName))
    summary = ia.summary()
    return summary['unit']

# BMAJ beam major axis in units of arcseconds
def getBmaj(imName):
    ia.open(str(imName))
    summary = ia.summary()
    major = summary['restoringbeam']['major']
    unit = summary['restoringbeam']['major']['unit']
    major_value = summary['restoringbeam']['major']['value']
    if unit == 'deg':
        major_value = major_value * 3600
    return major_value

# BMIN beam minor axis in units of arcseconds
def getBmin(imName):
    ia.open(str(imName))
    summary = ia.summary()
    minor = summary['restoringbeam']['minor']
    unit = summary['restoringbeam']['minor']['unit']
    minor_value = summary['restoringbeam']['minor']['value']
    if unit == 'deg':
        minor_value = minor_value * 3600
    return minor_value

# Position angle of the interferometeric data
def getPA(imName):
    ia.open(str(imName))
    summary = ia.summary()
    pa_value = summary['restoringbeam']['positionangle']['value']
    pa_unit  = summary['restoringbeam']['positionangle']['unit']
    return pa_value, pa_unit

# our Main, QAC style
def qac_ssc(project, highres=None, lowres=None, sdTel = None, regrid=True, label="", niteridx=0):
    """
        project     directory in which all work will be performed
        highres     high res (interferometer) image
        lowres      low res (SD/TP) image
        sdTEL       if not provided, sdFITS must contain the telescope
        regrid      if you are sure of the same WCS, set this to False
    """
    if niteridx == 0:
        niter_label = ""
    else:
        # otherwise the niter label reflect the tclean naming convention
        # e.g. tclean used niter = [0, 1000, 2000] and returned dirtymap, dirtymap_2, and dirtymap_3
        # to get the second iteration of tclean (niter=1000), niteridx = 1
        niter_label = "_%s"%(niteridx + 1)

    if highres == None:
        highres = "%s/dirtymap%s.image" % (project,niter_label)
    if lowres == None:
        lowres  = "%s/otf%s.image"    % (project,label)   
    
    print 'SSC array combination method'
    print '   Single-dish: ',lowres
    print '   Interferometer: ',highres
    print '   Single-dish Telescope: ',sdTel

    # Creating the prefix for all the CASA-images
    prefix = project + '/'

    lr = lowres                                  # input low resolution cube
    hr = highres                                 # input high resolution cube

    # temp files
    lr_reg    = prefix + 'LR_reg.im'             # regridded low resolution cube
    hr_conv   = prefix + 'HR_conv.im'            # convolved high resolution cube
    sub       = prefix + 'sub.im'                # observed flux only by single-dish
    sub_bc    = prefix + 'sub_bc.im'             # Corrected flux by the ratio of beam sizes
    clean_up  = [lr_reg, hr_conv, sub, sub_bc]   # collect filenames we need to clean

    # final results
    combined  = prefix + 'ssc%s%s.image'  % (label,niter_label)

    # Re-gridding the lowres Single-dish cube to that of the highres Interferometer cube
    if regrid:
        print 'Regridding ... the default interpolation scheme is linear'
        imregrid(lr,hr,lr_reg, overwrite=True)
    else:
        lr_reg = lr


    # Check if both data sets are in the same units
    if str(getBunit(lr_reg)) != str(getBunit(hr)):
        print 'Bunits of low- and high-resolution data cubes are not identical!'
        return

    print ''
    print 'LR_Bmin: ' + str(getBmin(lr_reg))
    print 'LR_Bmaj: ' + str(getBmaj(lr_reg))
    print ''
    print 'HR_Bmin: ' + str(getBmin(hr))
    print 'HR_Bmaj: ' + str(getBmaj(hr))
    print ''

    kernel1 = math.sqrt(float(getBmaj(lr_reg))**2 - float(getBmaj(hr))**2)
    kernel2 = math.sqrt(float(getBmin(lr_reg))**2 - float(getBmin(hr))**2)

    print 'Kernel1: ' + str(kernel1)
    print 'Kernel2: ' + str(kernel2)
    print ''

    # Convolve the highres with the appropriate beam so it matches the lowres 
    print 'Convolving high resolution cube ...'
    major = str(getBmaj(lr_reg)) + 'arcsec'
    minor = str(getBmin(lr_reg)) + 'arcsec'
    pa = str(getPA(hr)[0]) + str(getPA(hr)[1])
    print 'imsmooth',major,minor,pa
    imsmooth(hr, 'gauss', major, minor, pa, True, outfile=hr_conv, overwrite=True)

    # Missing flux
    print 'Computing the obtained flux only by single-dish ...'
    os.system('rm -rf %s' % sub)
    immath([lr_reg, hr_conv], 'evalexpr', sub, 'IM0-IM1')
    print 'Flux difference has been determined' + '\n'
    print 'Units', getBunit(lr_reg)

    if getBunit(lr_reg) == 'Jy/beam':
        print 'Computing the weighting factor according to the surface of the beam ...'
        weightingfac = (float(getBmaj(str(hr))) * float(getBmin(str(hr)))
                        ) / (float(getBmaj(str(lr_reg))) * float(getBmin(str(lr_reg))))
        print 'Weighting factor: ' + str(weightingfac) + '\n'

        print 'Considering the different beam sizes ...'
        os.system('rm -rf %s' % sub_bc)        
        immath(sub, 'evalexpr', sub_bc, 'IM0*' + str(weightingfac))
        print 'Fixed for the beam size' + '\n'

        print 'Combining the single-dish and interferometer cube [Jy/beam mode]'
        os.system('rm -rf %s' % combined)        
        immath([hr, sub_bc], 'evalexpr', combined, 'IM0+IM1')
        print 'The missing flux has been restored' + '\n'

    if getBunit(lr_reg) == 'Kelvin':
        print 'Combining the single-dish and interferometer cube [K-mode]'
        os.system('rm -rf %s' % combined)                
        immath([hr, sub], 'evalexpr', combined, 'IM0 + IM1')
        print 'The missing flux has been restored' + '\n'

    for f in clean_up:
        print "cleaning ",f
        os.system('rm -rf %s' % f)

    if True:
        qac_stats(lowres)
        qac_stats(highres)
        qac_stats(combined)

