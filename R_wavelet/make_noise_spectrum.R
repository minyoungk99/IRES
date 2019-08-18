#Create spectra for IRES report
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)
source('adv_biwavelet_packages.R')

#data <- rnorm(2000, sd=.5) + rep(c(rep(0, 99),10), 20)
data <- read.table('gaussian.txt')

wt_obj <- wt(cbind(1:714,as.numeric(data[,1])), lag1=.00000001)

par(oma = c(0, 0, 0, 1), mar = c(5, 4, 4, 5) + 0.1)
cmap = cm.colors(100)
plot.biwavelet_adv(wt_obj, plot.cb=TRUE, ncol=100, fill.cols=cmap, lwd.sig=1,)
