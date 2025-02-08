import numpy as np

a = np.arange(1, 6)
b = np.arange(6, 11)
print("add: ", a + b)
print("sub: ", a - b)
print("mul: ", a * b)
print("div: ", a / b)

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("original matrix: \n", matrix)

# transpose
transpose = matrix.T
print("transpose: \n", transpose)
print("add: ", matrix + transpose)
print("sub: ", matrix - transpose)
print("mul: ", matrix * transpose)
print("div: ", matrix / transpose)


arr4 = np.ones((4,5))
print(arr4)
print(np.sum(arr4, 0))
print(np.sum(arr4, 1))


arr_not_normalized = np.arange(0, 101)
arr_min = np.min(arr_not_normalized)
arr_max = np.max(arr_not_normalized)

normalized_arr = (arr_not_normalized - arr_min) / (arr_max - arr_min)
print(normalized_arr)