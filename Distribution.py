import scipy.stats as stats
probability_1 = stats.poisson.pmf(6,10)
print(f"Probability of raining for exactly 6 days {probability_1}")
probability_2 = stats.poisson.pmf(12,10)+stats.poisson.pmf(13,10)+stats.poisson.pmf(14,10)
print(f"Probability of raining for 12-14 days {probability_2}")