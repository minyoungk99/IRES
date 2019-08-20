#Create spectra for IRES report
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)
source('adv_biwavelet_packages.R')

#data <- rnorm(2000, sd=.5) + rep(c(rep(0, 99),10), 20)
#data <- read.table('fake_diffs.txt')
data <- read.table('../data/DOG1.txt')

par(oma = c(0, 0, 0, 1), mar = c(5, 4, 4, 5) + 0.1)
cmap = cm.colors(100)

#pdf('../plots/fake_diffs.pdf', width=5, height=3)
for (i in 1:1) {
  par(oma = c(0, 0, 0, 1), mar = c(5, 4, 4, 5) + 0.1)
  wt_obj <- wt(cbind(1:512,as.numeric(data[,1])), lag1=.00000001)
  plot.biwavelet_adv(wt_obj, plot.cb=TRUE, ncol=100, fill.cols=cmap, lwd.sig=1)
}
#dev.off()
