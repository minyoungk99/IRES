setwd('/Users/MYK/Desktop/IRES/R_wavelet')
library('WaveletComp')

#real data, 34minute runtime
#mjd <- read.table('J0332_timegrid.txt')
timeser <- read.table('J0332_timeser.txt')[1:714,1]

#fake data
#mstime <- read.table('fake_timegrid.txt')
#timeser <- read.table('fake_timeser.txt')

#create dataframe, label columns, specifically 'date' for analyze.wavelet function
df <- data.frame(1:714, timeser)
colnames(df) <- c('date', 'timeser')

my_wt <- analyze.wavelet(my.data=df, my.series="timeser", n.sim=10)

#labels is the actual label displayed, display int MJDs
#at is the indices to display the labels
time_axis = list(at=seq(0, 714, by=100), 
        labels = seq(0, .714, by=.1 ))

period_axis = list(at=2^(1:16), labels=2^(1:16)/1000)

par(mar = c(6.5, 6.5, 0.5, 0.5), mgp = c(5, 1, 0))
wt.image(my_wt, spec.time.axis=time_axis, spec.period.axis=period_axis,
         periodlab='Fourier Period (s)', timelab='Time (s)',
         color.palette='terrain.colors(100)', plot.ridge=FALSE,
         plot.contour=FALSE)
#wt.avg(my_wt)

#20min smoothing, 3min per simulation
