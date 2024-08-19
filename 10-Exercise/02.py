'''
A manufacturer says the Z-Phone smart phone has a mean consumer life of 42
months with a standard deviation of 8 months. Assuming a normal distribution,
what is the probability a given random Z-Phone will last between 20 and 30
months?
'''
from scipy.stats import norm
mean = 42
standard_deviation = 8
x = norm.cdf(30, mean, standard_deviation) - norm.cdf(20, mean, standard_deviation)
print(x)

