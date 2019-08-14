#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
library('biwavelet')

x <- matrix(1:714, nrow=1)
ratios <- read.table('J0332_ratios.txt')
#combine these two into 2x714 matrix required format for wt.sig



