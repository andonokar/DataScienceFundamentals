import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("std: ", np.std(arr))
print("sum rows: ", np.sum(arr, 1))
print("sum columns: ", np.sum(arr, 0))