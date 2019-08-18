#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)
source('adv_biwavelet_packages.R')

timeseries <- read.table('J0332_nogap_timeser.txt')
nbins <- dim(timeseries)[1]
cum_sig <- .99
data <- cbind(1:nbins, sapply(timeseries[,1], FUN=as.numeric))

#MODIFY generate_red as applicable
#Arcwise testing
wt <- wt_arc(data, lag1=.0000000001, asig.level=cum_sig)
              #psig.level = c(0.82,.84,0.86,.88,0.90,.92,0.94,.96,0.98))
  
cmap = cm.colors(100)
par(oma = c(0, 0, 0, 1), mar = c(5, 4, 4, 5) + 0.1) #make space for colorbar
#pdf("../plots/J0332_arcwise.pdf", width=5, height=3) 
#jpeg("../plots/J0332_arcwise.jpeg")
plot.biwavelet_adv(wt,  plot.cb=TRUE, ncol=100, fill.cols=cmap, lwd.sig=1)
#dev.off()

