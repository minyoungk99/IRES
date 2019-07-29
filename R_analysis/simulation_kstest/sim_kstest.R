#Perform KS-test on discrete null and empirical distribution
setwd("/Users/MYK/Desktop/IRES/R_analysis/simulation_kstest")

null <- read.table('temp_a.txt')
data <- read.table('temp_b_sim.txt')
D_value <- c()

for (i in seq( dim(data)[1] )) {
  result <- ks.test(data[i,], ecdf(null[,1]))
  D_value[i] <- result$statistic
}

write.table(D_value, file = "temp_a_sim_b_Dvalues.txt", row.names = FALSE,
            col.names = FALSE)