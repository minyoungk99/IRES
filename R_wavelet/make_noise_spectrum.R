#Create spectra for IRES report
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)

data <- rnorm(2000, sd=.5) + rep(c(rep(0, 99),10), 20)
wt_obj <- wt(cbind(1:2000,data), lag1=.00000001)
plot.biwavelet(wt_obj)
