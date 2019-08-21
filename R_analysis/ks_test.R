#Perform KS-test on discrete null and empirical distribution
setwd("/Users/MYK/Desktop/IRES/R_analysis")

null <- read.table('null.txt')
data <- read.table('sim_cdf.txt')
D_value <- c()

for (i in seq( dim(data)[1] )) {
  result <- ks.test(data[i,], ecdf(null[,1]))
  D_value[i] <- result$statistic
}

write.table(D_value, file = "sim_Dvalues.txt", row.names = FALSE,
            col.names = FALSE)