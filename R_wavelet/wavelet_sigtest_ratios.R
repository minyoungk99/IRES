#Perform wavelet significance test on profile ratios
setwd("/Users/MYK/Desktop/IRES/R_wavelet")
packages <- c('biwavelet', 'pracma', 'fields', 'RColorBrewer') #'fields' required for plotting colorbar
lapply(packages, FUN=library, character.only=TRUE)
source('adv_biwavelet_packages.R')

mjd <- read.table('../data/J0332_MJD.txt')
mjd <- mjd[-1,1] #drop first MJD
profs <- read.table('../data/J0332_profs.txt')
ratios <- read.table('J0332_ratios.txt')
#combine these two into 714x2 matrix required format for wt.sig
#convert each observation of a variable to numeric by sapply(ratios[1,], MARGIN=1,FUN=as.numeric)

#EDIT FUNCTION GENERATE_REDNOISE IN adv_biwavelet_packages.R to use RATIO of WN 
#change d1 <- whatever to d1 <- cbind(ntseq,
#ar1_ma0_sim(mr1, lag1[1], ntimesteps)/ar1_ma0_sim(mr1, lag1[1], ntimesteps))
#in last line of generate_red()

nprofs <- dim(ratios)[1]
nbins <- dim(ratios)[2]
cum_sig <- .99

pdf("../plots/ratio_99.pdf", width=5, height=3) 
cmap = cm.colors(64)
for (i in 1:nprofs) {
  par(oma = c(0, 0, 0, 1), mar = c(5, 4, 4, 5) + 0.1) #make space for colorbar
  data <- cbind(1:nbins, sapply(ratios[i,], FUN=as.numeric))
  wt <- wt_area(data, lag1=.0000000001,  csig.level=cum_sig, 
                psig.level = c(0.82,.84,0.86,.88,0.90,.92,0.94,.96,0.98))
  plot.biwavelet_adv(wt,  plot.cb=TRUE, ncol=64, fill.cols=cmap, lwd.sig=1,
                     main=bquote("MJD:" ~ .(mjd[i])*","~ alpha[cum]*":"~.(1-cum_sig)))
}
dev.off()

