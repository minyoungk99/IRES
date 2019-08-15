#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
library('biwavelet')
library('pracma')
source('adv_biwavelet_packages.R')

mjd <- read.table('../J0332_MJD.txt')
mjd <- mjd[-1,1][1] #drop first MJD
ratios <- read.table('J0332_ratios.txt')
#combine these two into 2x714 matrix required format for wt.sig
#convert each observation of a variable to numeric by sapply(ratios[1,], MARGIN=1,FUN=as.numeric)



