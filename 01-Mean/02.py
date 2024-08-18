sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40]
weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights)
print(weighted_mean)
print(sum(sample)/len(sample)) # simple mean