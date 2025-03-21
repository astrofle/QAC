# -*- makefile -*-
#
#  Example targets to run a set of ngVLA simulations
#

TESTS = test1 test1a test2 test1-alma test1-SSA test5 vla1 vla2 \
	figures

help:	
	@echo no help

.PHONY:   $(TESTS)

all:	$(TESTS)

#  test targets

test1:
	time casa --nogui -c test1.py > test1.log 2>&1

test1a:
	time casa --nogui -c test1a.py > test1a.log 2>&1

test1-alma:
	rm -rf test1-alma
	time casa --nogui -c test1-alma.py > test1-alma.log 2>&1

test1-SSA:
	rm -rf test1-SSA
	time casa --nogui -c test1-SSA.py > test1-SSA.log 2>&1

test2:
	rm -rf test2
	time casa --nogui -c test2.py > test2.log 2>&1

test5:
	rm -rf test5
	time casa --nogui -c test5.py > test5.log 2>&1

vla1:
	rm -rf vla1
	time casa --nogui -c vla1.py > vla1.log 2>&1

# ---------------------------------------------------------------------------------------------
vla2:
	rm -rf vla2
	time casa --nogui -c vla2.py > vla2.log 2>&1
	cp vla2.log vla2.py vla2.ptg vla2
	tail -10 vla2.log

VLA2_ALL = vla2_0     vla2_1     vla2_01 \
	   vla2_0g_45 vla2_1g_45 vla2_01g_45 \
	   vla2_0g_18 vla2_1g_18 vla2_01g_18

vla2_all:	$(VLA2_ALL)

vla2_all_clean:
	rm -rf 	$(VLA2_ALL)

# single pointing tests
vla2_0:
	time casa --nogui -c vla2.py pdir='"vla2_0"' cfg='[0]' grid=0 pixel_m=0.02 pixel_s=0.04   > vla2.log 2>&1
	cp vla2.log vla2.py vla2_0.ptg vla2_0
	tail -10 vla2.log

vla2_1:
	time casa --nogui -c vla2.py pdir='"vla2_1"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 > vla2_1.log 2>&1
	# test targets:
	#time casa --nogui -c vla2.py pdir='"vla2_1"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=1024 pixel_s=0.02 > vla2_1_b.log 2>&1      # _b
	#time casa --nogui -c vla2.py pdir='"vla2_1"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=2048 pixel_s=0.01 > vla2_1_c.log 2>&1      # _c

# test when clean converges, the default only does 500,1000,2000,4000
# but these long ones showed the flux converges to different answers,and even diverges... why?
vla2_1_long:
	time casa --nogui -c vla2.py pdir='"vla2_1_long"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 niter='range(0,20000,1000)' > vla2_1_long.log 2>&1
vla2_1_long_a:
	time casa --nogui -c vla2.py pdir='"vla2_1_long_a"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=256 niter='range(0,20000,1000)' > vla2_1_long_a.log 2>&1
vla2_1_long_b:
	time casa --nogui -c vla2.py pdir='"vla2_1_long_b"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=256 niter='range(0,20000,1000)' scales='[0,5,10,20,40]' > vla2_1_long_b.log 2>&1

# series of single pointing mosaics with varying dish (0.006 probably better, 0.008 fails in fidelity)
vla2_1_dish:
	time casa --nogui -c vla2.py pdir='"vla2_1_18"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 dish=18 > vla2_1_18.log 2>&1
	time casa --nogui -c vla2.py pdir='"vla2_1_30"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 dish=30 > vla2_1_30.log 2>&1
	time casa --nogui -c vla2.py pdir='"vla2_1_45"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 dish=45 > vla2_1_45.log 2>&1
	time casa --nogui -c vla2.py pdir='"vla2_1_100"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 dish=100 > vla2_1_100.log 2>&1
	time casa --nogui -c vla2.py pdir='"vla2_1_200"' cfg='[1]' grid=0 pixel_m=0.005 imsize_s=512 dish=200 > vla2_1_200.log 2>&1

vla2_01:
	time casa --nogui -c vla2.py pdir='"vla2_01"' cfg='[0,1]' grid=0 pixel_m=0.005 imsize_s=512 pixel_s=0.04 > vla2_01.log 2>&1
	cp vla2_01.log vla2.py vla2_01.ptg vla2_01
	tail -10 vla2_01.log


vla2_1_all: vla2_1_d vla2_1_e vla2_1_f vla2_1_g

vla2_1_d:
	time casa --nogui -c vla2.py pdir='"vla2_1_d"' cfg='[1]' pixel_m=0.005 imsize_s=512 pfactor=2.0 > vla2_1_d.log 2>&1 

vla2_1_e:
	time casa --nogui -c vla2.py pdir='"vla2_1_e"' cfg='[1]' pixel_m=0.005 imsize_s=512 pfactor=3.0 > vla2_1_e.log 2>&1 

vla2_1_f:
	time casa --nogui -c vla2.py pdir='"vla2_1_f"' cfg='[1]' pixel_m=0.005 imsize_s=512 pfactor=4.0 > vla2_1_f.log 2>&1 

vla2_1_g:
	time casa --nogui -c vla2.py pdir='"vla2_1_g"' cfg='[1]' pixel_m=0.005 imsize_s=512 pfactor=5.0 > vla2_1_g.log 2>&1 



# same, for default filled grid, with TP=45m
vla2_0g_45:
	time casa --nogui -c vla2.py pdir='"vla2_0g_45"' cfg='[0]' dish=45 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_0g_45.ptg vla2_0g_45
	tail -10 vla2.log

vla2_1g_45:
	time casa --nogui -c vla2.py pdir='"vla2_1g_45"' cfg='[1]' dish=45 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_1g_45.ptg vla2_1g_45
	tail -10 vla2.log

vla2_01g_45:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45"' cfg='[0,1]' dish=45 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45
	tail -10 vla2.log

vla2_01g_45_flip:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_flip"' cfg='[0,1]' dish=45 afactor=-1 niter='[0,1000]' > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_flip
	tail -10 vla2.log

vla2_01g_45_amp11:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_amp11"' cfg='[0,1]' dish=45 afactor=1.1 niter='[0,1000]' > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_amp11
	tail -10 vla2.log

vla2_01g_45_amp12:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_amp12"' cfg='[0,1]' dish=45 afactor=1.2 niter='[0,1000]' > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_amp12
	tail -10 vla2.log

vla2_01g_45_amp13:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_amp13"' cfg='[0,1]' dish=45 afactor=1.3 niter='[0,1000]' > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_amp13
	tail -10 vla2.log

vla2_01g_45_a:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_a"' cfg='[0,1]' dish=45 wfactor=0.02 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_a
	tail -10 vla2.log

vla2_01g_45_b:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_b"' cfg='[0,1]' dish=45 wfactor=0.02 pixel_m=0.025 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_b
	tail -10 vla2.log

vla2_01g_45_c:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_c"' cfg='[0,1]' dish=45 wfactor=0.02 pixel_m=0.025 times='[8,1]' > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_c
	tail -10 vla2.log

vla2_01g_45_d:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_d"' cfg='[0,1]' dish=45 wfactor=0.02 pixel_m=0.025 grid=10 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_d
	tail -10 vla2.log

# weight factor between SBA and core

vla2_01g_45_scales: vla2_01g_45_e vla2_01g_45_f vla2_01g_45_g vla2_01g_45_h vla2_01g_45_i vla2_01g_45_j vla2_01g_45_k vla2_01g_45_l

vla2_01g_45_e:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_e"' cfg='[0,1]' wfactor=0.5 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_e
	tail -10 vla2.log

vla2_01g_45_f:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_f"' cfg='[0,1]' wfactor=0.2 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_f
	tail -10 vla2.log

vla2_01g_45_g:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_g"' cfg='[0,1]' wfactor=0.1 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_g
	tail -10 vla2.log

vla2_01g_45_h:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_h"' cfg='[0,1]' wfactor=0.05  > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_h
	tail -10 vla2.log

vla2_01g_45_i:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_i"' cfg='[0,1]' wfactor=0.02  > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_i
	tail -10 vla2.log

vla2_01g_45_j:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_j"' cfg='[0,1]' wfactor=0.01  > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_j
	tail -10 vla2.log

vla2_01g_45_k:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_k"' cfg='[0,1]' wfactor=0.001  > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_k
	tail -10 vla2.log

vla2_01g_45_l:
	time casa --nogui -c vla2.py pdir='"vla2_01g_45_l"' cfg='[0,1]' wfactor=0.0001  > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45.ptg vla2_01g_45_l
	tail -10 vla2.log


# same, for default filled grid, with TP=18m
vla2_0g_18:
	time casa --nogui -c vla2.py pdir='"vla2_0g_18"' cfg='[0]' dish=18 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_0g_18.ptg vla2_0g_18
	tail -10 vla2.log

vla2_1g_18:
	time casa --nogui -c vla2.py pdir='"vla2_1g_18"' cfg='[1]' dish=18 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_1g_18.ptg vla2_1g_18
	tail -10 vla2.log

vla2_01g_18:
	time casa --nogui -c vla2.py pdir='"vla2_01g_18"' cfg='[0,1]' dish=18 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_18.ptg vla2_01g_18
	tail -10 vla2.log

# JT versions (about 30' per sim)
vla2_01g_18_jt:
	time casa --nogui -c vla2.py    pdir='"vla2_01g_18_jt"' cfg='[0,1]' pixel_m=0.05 imsize_s=1024 dish=18 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_18_jt.ptg vla2_01g_18_jt
	tail -10 vla2.log

vla2_01g_45_jt:
	time casa --nogui -c vla2.py    pdir='"vla2_01g_45_jt"' cfg='[0,1]' pixel_m=0.05 imsize_s=1024 dish=45 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_45_jt.ptg vla2_01g_45_jt
	tail -10 vla2.log

# same, for default filled grid, with TP=100m
vla2_0g_100:
	time casa --nogui -c vla2.py pdir='"vla2_0g_100"' cfg='[0]' dish=100 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_0g_100.ptg vla2_0g_100
	tail -10 vla2.log

vla2_1g_100:
	time casa --nogui -c vla2.py pdir='"vla2_1g_100"' cfg='[1]' dish=100 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_1g_100.ptg vla2_1g_100
	tail -10 vla2.log

vla2_01g_100:
	time casa --nogui -c vla2.py pdir='"vla2_01g_100"' cfg='[0,1]' dish=100 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_01g_100.ptg vla2_01g_100
	tail -10 vla2.log

# simple noise test on cfg=0
noise:  vla2_noise0 vla2_noise1

vla2_noise0:
	time casa --nogui -c vla2.py 'cfg=[0]' noise=1000000 pdir="'vla2_noise0'" niter='[0,1000]' > vla2_noise0.log 2>&1

vla2_noise1:
	time casa --nogui -c vla2.py 'cfg=[1]' noise=1000000 pdir="'vla2_noise1'" niter='[0,1000]' > vla2_noise1.log 2>&1

#
vla2_0g_18_noise:
	time casa --nogui -c vla2.py pdir='"vla2_0g_18_noise"' cfg='[0]' dish=18 noise=150 > vla2.log 2>&1
	cp vla2.log vla2.py vla2_0g_18_noise.ptg vla2_0g_18_noise
	tail -10 vla2.log

#
vla2_noise:
	time casa --nogui -c vla2.py 'cfg=[0]' noise=0  pdir="'vla2_noise_0'" niter='[0,1000]' > vla2_noise_0.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=25 pdir="'vla2_noise_a'" niter='[0,1000]' > vla2_noise_a.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=50 pdir="'vla2_noise_b'" niter='[0,1000]' > vla2_noise_b.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=75 pdir="'vla2_noise_c'" niter='[0,1000]' > vla2_noise_c.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=100 pdir="'vla2_noise_d'" niter='[0,1000]' > vla2_noise_d.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=125 pdir="'vla2_noise_e'" niter='[0,1000]' > vla2_noise_e.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=150 pdir="'vla2_noise_f'" niter='[0,1000]' > vla2_noise_f.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=175 pdir="'vla2_noise_g'" niter='[0,1000]' > vla2_noise_g.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=200 pdir="'vla2_noise_h'" niter='[0,1000]' > vla2_noise_h.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=225 pdir="'vla2_noise_i'" niter='[0,1000]' > vla2_noise_i.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=250 pdir="'vla2_noise_j'" niter='[0,1000]' > vla2_noise_j.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=500 pdir="'vla2_noise_k'" niter='[0,1000]' > vla2_noise_k.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=1000 pdir="'vla2_noise_l'" niter='[0,1000]' > vla2_noise_l.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=10000 pdir="'vla2_noise_m'" niter='[0,1000]' > vla2_noise_m.log 2>&1
	time casa --nogui -c vla2.py 'cfg=[0]' noise=100000 pdir="'vla2_noise_n'" niter='[0,1000]' > vla2_noise_n.log 2>&1

# test on wider array, but only map inner portion

PLAINS = plains_0 plains_2 plains_02

plains_all: $(PLAINS)

plains_all_clean:
	rm -rf $(PLAINS)

plains_0:
	time casa --nogui -c vla2.py 'cfg=[0]' pdir="'plains_0'" niter='[0,1000]' dish=45 \
	     pixel_m=0.01 imsize_s=2048 pixel_s=0.02 \
	     > plains_0.log 2>&1

plains_2:
	time casa --nogui -c vla2.py 'cfg=[2]' pdir="'plains_2'" niter='[0]' grid=0 dish=45 \
	     times='[8,1]' \
	     pixel_m=0.005 imsize_s=2048 pixel_s=0.005 \
	     > plains_2.log 2>&1

plains_2a:
	time casa --nogui -c vla2.py 'cfg=[2]' pdir="'plains_2a'" niter='[0]' grid=0 dish=45 \
	     times='[8,1]' \
	     pixel_m=0.005 imsize_s=2048 pixel_s=0.0025 \
	     > plains_2a.log 2>&1

plains_02:
	time casa --nogui -c vla2.py 'cfg=[0,2]' pdir="'plains_02'" niter='[0,1000]' dish=45 \
	     pixel_m=0.01 imsize_s=2048 pixel_s=0.02 \
	     > plains_02.log 2>&1

# test on an even wider array

MAIN = main_0 main_3 main_03

main_all: $(MAIN)

main_all_clean:
	rm -rf $(MAIN)


main_0:
	time casa --nogui -c vla2.py 'cfg=[0]' pdir="'main_0'" niter='[0,1000]' dish=45 \
	     pixel_m=0.01 imsize_s=2048 pixel_s=0.02 \
	     > main_0.log 2>&1

main_3:
	time casa --nogui -c vla2.py 'cfg=[3]' pdir="'main_3'" niter='[0]' dish=45 \
	     times='[8,1]' \
	     pixel_m=0.0001 imsize_s=2048 pixel_s=0.0001 \
	     > main_3.log 2>&1

main_03:
	time casa --nogui -c vla2.py 'cfg=[0,3]' pdir="'main_03'" niter='[0,1000]' dish=45 \
	     pixel_m=0.01 imsize_s=2048 pixel_s=0.02 \
	     > main_03.log 2>&1

# figures for talk?
figures:  figures_jt
	mkdir -p figures
	cp vla2_01g_45_d/vla2_01g_45_d.psd_3.png             figures/psd0.png
	cp vla2_1g_18/clean3/dirtymap_6.image.pbcor.png      figures/map1.png
	cp vla2_01g_18/clean3/dirtymap_6.image.pbcor.png     figures/map2.png
	cp vla2_1g_45/clean3/feather45_6.image.pbcor.png     figures/map3.png
	cp vla2_01g_45/clean3/feather45_6.image.pbcor.png    figures/map4.png
	cp vla2_1g_18/clean3/feather18_6.image.pbcor.png     figures/map5.png
	cp vla2_01g_18/clean3/feather18_6.image.pbcor.png    figures/map6.png
	#
	cp vla2_1_45/plot2.cmp.png                           figures/fig1.png
	cp vla2_1_45/vla2_1_45.ngvla-core-revB.observe.png   figures/fig2.png
	cp vla2_1_g/clean3/dirtymap_6.image.pbcor.png        figures/fig4.png
	cp vla2_1_g/plot2.cmp.png                            figures/fig5.png

figures_flow:
	#  flow diagram
	cp vla2_1g_45/clean3/skymodel.rebin.image.png             figures/flow1.png
	cp vla2_1g_45/clean3/dirtymap.image.pbcor.png             figures/flow2.png
	cp vla2_1g_45/clean3/dirtymap_6.image.pbcor.png           figures/flow3.png
	cp vla2_1g_45/clean3/skymodel.smooth.image.png            figures/flow4.png
	cp vla2_1g_45/clean3/feather45_6.image.pbcor.png          figures/flow5.png
	cp vla2_1g_45/clean3/feather45_6.image.pbcor.diff.png     figures/flow6.png
	cp vla2_1g_45/clean3/otf45.image.pbcor.png                figures/flow7.png
	cp vla2_1g_45/clean3/feather45_6.image.pbcor.fidelity.png figures/flow8.png


figures_jt_old:
	# Jordan's plots in the poster (need to replace this with the 0.05 pixel size, not the 0.025 which is the default)
	cp vla2_01g_45/vla2_01g_45.ngvla-sba-revB.skymodel.png    figures/jt1a1.png
	cp vla2_01g_45/vla2_01g_45.ngvla-sba-revB.observe.png     figures/jt1a2.png
	cp vla2_01g_45/vla2_01g_45.ngvla-core-revB.skymodel.png   figures/jt1b1.png
	cp vla2_01g_45/vla2_01g_45.ngvla-core-revB.observe.png    figures/jt1b2.png
	cp vla2_01g_45/clean3/dirtymap_6.image.pbcor.png          figures/jt2.png
	cp vla2_01g_18/clean3/otf18.image.pbcor.png          	  figures/jt3a.png
	cp vla2_01g_45/clean3/otf45.image.pbcor.png          	  figures/jt3b.png
	cp vla2_01g_45/clean3/skymodel.smooth.image.png           figures/jt4.png
	cp vla2_01g_18/clean3/feather18_6.image.pbcor.png         figures/jt5a.png
	cp vla2_01g_45/clean3/feather45_6.image.pbcor.png         figures/jt5b.png

figures_jt:
	# Jordan's plots in the poster (need to replace this with the 0.05 pixel size, not the 0.025 which is the default)
	cp vla2_01g_45_jt/vla2_01g_45_jt.ngvla-sba-revB.skymodel.png    figures/jt1a1.png
	cp vla2_01g_45_jt/vla2_01g_45_jt.ngvla-sba-revB.observe.png     figures/jt1a2.png
	cp vla2_01g_45_jt/vla2_01g_45_jt.ngvla-core-revB.skymodel.png   figures/jt1b1.png
	cp vla2_01g_45_jt/vla2_01g_45_jt.ngvla-core-revB.observe.png    figures/jt1b2.png
	cp vla2_01g_45_jt/clean3/dirtymap_6.image.pbcor.png             figures/jt2.png
	cp vla2_01g_18_jt/clean3/otf18.image.pbcor.png          	figures/jt3a.png
	cp vla2_01g_45_jt/clean3/otf45.image.pbcor.png          	figures/jt3b.png
	cp vla2_01g_45_jt/clean3/skymodel.smooth.image.png              figures/jt4.png
	cp vla2_01g_18_jt/clean3/feather18_6.image.pbcor.png         	figures/jt5a.png
	cp vla2_01g_45_jt/clean3/feather45_6.image.pbcor.png         	figures/jt5b.png
	cp vla2_01g_18_jt/clean3/feather18_6.image.pbcor.fidelity.png   figures/jt8a.png
	cp vla2_01g_45_jt/clean3/feather45_6.image.pbcor.fidelity.png   figures/jt8b.png
	cp vla2_01g_18_jt/vla2_01g_18_jt.psd.png                        figures/jt7a.png
	cp vla2_01g_45_jt/vla2_01g_45_jt.psd.png                        figures/jt7b.png

# jupiter test ;    courtesey: Chris Moeckel <chris.moeckel@berkeley.edu>

jup1:
	time casa --nogui -c vla2.py pdir="'jup1'" model="'Jupiter_scaled_structur_0.08as.fits'"  \
		imsize_m=5040 pixel_m=0.03 imsize_s=512 \
		cfg='[1]' grid=0   > jup1.log  2>&1 

jup2:
	time casa --nogui -c vla2.py pdir="'jup2'" model="'Jupiter_scaled_structur_0.08as.fits'"  \
		imsize_m=5040 pixel_m=0.03 imsize_s=512 dish=100 \
		cfg='[1]' grid=0   > jup2.log  2>&1


# simple mapping scripts to start studying ngVLA project for students
# mapping0,1 have no short spacing added, they are fun to play with, but
# (should) give lousy results for Fidelity and such
#
# Clone the targets mapping0, mapping1 to create your own experiments in your own Makefile (e.g. Sarafile)
# so you can run them as:       make -f Sarafile exp1 exp2
#
mapping0:
	time casa -c mapping0.py > mapping0.log 2>&1
	tail -10 mapping0.log

mapping1:
	time casa -c mapping1.py > mapping1.log 2>&1
	tail -10 mapping1.log

mapping2:
	time casa -c mapping2.py grid=15 pixel_m=0.01 clean=0  > mapping2.log 2>&1
	tail -10 mapping2.log

mapping3:
	time casa -c mapping3.py > mapping3.log 2>&1
	tail -10 mapping3.log

# point source
point1:
	time casa --nogui -c mapping1.py pdir="'point1'" model="'../models/point.fits'" niter='range(0,10,1)' > point1.log 2&>1
	mv point1.log point1
	./plot_niter log=point1/point1.log out=point1/point1.tab

# reproduce casa crash while running for galaxy model0
gal_bug1:
	time casa --nogui -c galaxy1.py pdir="'gal1'" model="'../models/model0.fits'" imsize_m=192 pixel_m=0.5 imsize_s=192 pixel_s='-1' niter='[0,1000]' cfg='[0,1]' grid=15 dish=45 scales='[0]'  > gal1.log 2&1>1
