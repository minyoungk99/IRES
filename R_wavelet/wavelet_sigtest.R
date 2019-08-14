#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
library('biwavelet')
source('adv_biwavelet_packages.R')

x <- matrix(1:714, nrow=1)
mjd <- read.table('../J0332_MJD.txt')
mjd <- mjd[-1,1][1] #drop first MJD
ratios <- read.table('J0332_ratios.txt')
#combine these two into 2x714 matrix required format for wt.sig



