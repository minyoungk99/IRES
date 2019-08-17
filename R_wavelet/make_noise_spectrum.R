#Create spectra for IRES report
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)

data <- rnorm(1000)
wt_obj <- wt(cbind(1:1000,data), lag1=.00000001)
dev.off()
plot.biwavelet(wt_obj)
