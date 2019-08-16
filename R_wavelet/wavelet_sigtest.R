#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)
source('adv_biwavelet_packages.R')

mjd <- read.table('../J0332_MJD.txt')
mjd <- mjd[-1,1] #drop first MJD
profs <- read.table('../J0332_profs.txt')
ratios <- read.table('J0332_ratios.txt')
#combine these two into 714x2 matrix required format for wt.sig
#convert each observation of a variable to numeric by sapply(ratios[1,], MARGIN=1,FUN=as.numeric)

nprofs <- 1#dim(ratios)[1]
nbins <- dim(ratios)[2]
pw_sig <- .99
cum_sig <- .99

pdf("../plots/ratio_power_spectra.pdf", width=5, height=3) 
cmap = cm.colors(64)
for (i in 1:nprofs) {
  par(oma = c(0, 0, 0, 1), mar = c(5, 4, 4, 5) + 0.1) #make space for colorbar
  data <- cbind(1:nbins, sapply(ratios[i,], FUN=as.numeric))
  wt <- wt_area(data, lag1=.0000000000001, sig.level = pw_sig, csig.level=cum_sig)
  plot.biwavelet_adv(wt,  plot.cb=TRUE, ncol=64, fill.cols=cmap,
                     main=bquote("MJD:" ~ .(mjd[i])*","~alpha[pw]*":"~.(pw_sig)*","~
                                   alpha[cum]*":"~.(cum_sig)))
}
dev.off()

