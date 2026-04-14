import scipy.stats as stats
probability_1= stats.poisson.cdf(20,15)
print(f"Probability of getting 20 calls while average is 15 is {probability_1}")                 
probability_2 = stats.poisson.cdf(21,15)-stats.poisson.cdf(16, 15)
print(probability_2)