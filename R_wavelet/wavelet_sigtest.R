#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)
source('adv_biwavelet_packages.R')

mjd <- read.table('../J0332_MJD.txt')
mjd <- mjd[-1,1][1] #drop first MJD
ratios <- read.table('J0332_ratios.txt')
#combine these two into 2x714 matrix required format for wt.sig
#convert each observation of a variable to numeric by sapply(ratios[1,], MARGIN=1,FUN=as.numeric)

i <- 3
wt_obj <- wt_area(cbind(1:714, sapply(ratios[i,], MARGIN=1, FUN=as.numeric)), 
                        lag1=.00000001, Nnull=10000, anrands = 1000)
plot.biwavelet_adv(wt_obj)

