setwd('/Users/MYK/Desktop/IRES/R_wavelet')
library('WaveletComp')

#real data, 34minute runtime
#timeser <- read.table('J0332_timeser.txt')
#timeser <- timeser[1:714,1]
morlet <- sapply(read.table('../data/morlet.txt')[,1], FUN=as.numeric)

#create dataframe, label columns, specifically 'date' for analyze.wavelet function
df <- data.frame(seq(1, length(morlet)), morlet)
colnames(df) <- c('date', 'timeser')

my_wt <- analyze.wavelet(my.data=df, my.series="timeser", n.sim=10)

#labels is the actual label displayed, display int MJDs
#at is the indices to display the labels
#time_axis = list(at=seq(0, 714, by=50), 
#                 labels = seq(0, .714, by=.05))

#period_axis = list(at=2^(1:7), labels=sapply( round(2^(1:7)/714,3), FUN=as.numeric ))
par(mar = c(5, 6.5, 0.5, 0.5), mgp = c(3.5, 1, 0))
wt.image(my_wt,  timelab='Time', periodlab='Period', 
         plot.contour=FALSE, plot.ridge=FALSE)

