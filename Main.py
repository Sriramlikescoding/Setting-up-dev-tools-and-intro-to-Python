import scipy.stats as stats
cdf = 1-stats.binom.cdf(6,10,0.5)
print(f"Probability of getting more than 6 heads in 10 flips is {cdf}")