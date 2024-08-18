from math import sqrt
sample =  [0, 1, 5, 7, 9, 10, 14]
def variance(values):
    mean = sum(values)/len(values)
    _variance = 0
    for i in range(len(values)):
        _variance+=((values[i]-mean)**2) / len(values)
    return _variance
def std_dev(values):
    return sqrt(variance(values))

print(std_dev(sample))