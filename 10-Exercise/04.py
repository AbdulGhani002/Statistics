'''
Your marketing department has started a new advertising campaign and wants to
know if it affected sales, which in the past averaged $10,345 a day with a standard deviation of $552. The new advertising campaign ran for 45 days and averaged $11,641 in sales.
Did the campaign affect sales? Why or why not? (Use a two-tailed test for more reliable significance.)
'''
from scipy.stats import norm
mean = 10345
std_dev = 552
p1 = 1.0 - norm.cdf(11641, mean, std_dev)
p2 = p1
p_value = p1 + p2
print("Two-tailed P-value", p_value)
if p_value <= .05:
    print("Passed")
else:
    print("Failed")