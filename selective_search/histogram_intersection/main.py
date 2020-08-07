import numpy as np
import matplotlib.pyplot as plt

def return_intersection(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection


mu_1 = -4 # mean of the first distribution
mu_2 = 4  # mean of the second distribution
data_1 = np.random.normal(mu_1, 2.0, 1000)
data_2 = np.random.normal(mu_2, 2.0, 1000)
hist_1, bin_1 = np.histogram(data_1, bins=100, range=[-15,15])
hist_2, bin_2 = np.histogram(data_2, bins=100, range=[-15,15])

plt.plot(hist_1,bin_1[:-1])
plt.savefig("his.png")

print("test")