'''
I am skeptical that my 3D printer filament is not 1.75 mm in average diameter
as advertised. I sampled 34 measurements with my tool. The sample mean is
1.715588 and the sample standard deviation is 0.029252.
What is the 99% confidence interval for the mean of my entire spool of filament?
'''
from math import sqrt
from scipy.stats import norm
def critical_z_value(p, mean=0.0, std=1.0):
    norm_dist = norm(loc=mean, scale=std)
    left_area = (1.0 - p) / 2.0
    right_area = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(left_area), norm_dist.ppf(right_area)
def ci_large_sample(p, sample_mean, sample_std, n):
 # Sample size must be greater than 30
    lower, upper = critical_z_value(p)
    lower_ci = lower * (sample_std / sqrt(n))
    upper_ci = upper * (sample_std / sqrt(n))
    return sample_mean + lower_ci, sample_mean + upper_ci
print(ci_large_sample(p=.99, sample_mean=1.715588,
 sample_std=0.029252, n=34))
