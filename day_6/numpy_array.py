import numpy as np
from scipy import stats

arr = np.array([12, 45, 23, 67, 34])
print("All elements in the array:", arr)
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)
mean = np.mean(arr)
median = np.median(arr)

mode_result = stats.mode(arr)
mode = np.asarray(mode_result.mode).ravel()[0]
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
