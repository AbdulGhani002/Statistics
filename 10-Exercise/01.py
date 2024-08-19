'''
You bought a spool of 1.75 mm filament for your 3D printer. You want to
measure how close the filament diameter really is to 1.75 mm. You use a caliper
tool and sample the diameter five times on the spool:
1.78, 1.75, 1.72, 1.74, 1.77
Calculate the mean and standard deviation for this set of values.
'''
from math import sqrt
def standard_deviation(data,mean:float):
    variance = sum((v - mean) ** 2 for v in data) / (len(data))
    return sqrt(variance)
data = [1.78, 1.75, 1.72, 1.74, 1.77]
mean = sum(data)/len(data)
print(mean)
print(standard_deviation(data,mean))