import numpy as np

arr = np.array([10, 20, 30, 40 ,50])
# indexing is equal to list
print(arr[2], arr[-1])

# slicing is equal to list
print(arr[1:4], arr[:3])

# reshape array
print(arr.reshape(2, 3))