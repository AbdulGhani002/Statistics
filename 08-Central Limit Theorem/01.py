import random
import plotly.express as px
sample_size = 31
sample_count = 1000
# Central limit theorem, 1000 samples each with 31
# random numbers between 0.0 and 1.0
x_values = [(sum([random.uniform(0.0, 1.0) for i in range(sample_size)]) / sample_size) for _ in range(sample_count)]
y_values = [1 for _ in range(sample_count)]
px.histogram(x=x_values, y = y_values, nbins=20).show()
'''
What does Central Limit Theorem States: 
1. The mean of the sample means is equal to the population mean.
2. If the population is normal, then the sample means will be normal.
3. If the population is not normal, but the sample size is greater than 30, the sample
means will still roughly form a normal distribution.
4. The standard deviation of the sample means equals the population standard
deviation divided by the square root of n:
sample standard deviation = population standard deviation / sqrt(sample size)'''