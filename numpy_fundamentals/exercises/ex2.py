import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([1, 0, -1])
result_add = matrix + vector
result_mult = matrix * vector

matrix_random = np.random.randint(1, 51, (5,5))
print(matrix_random)

print(matrix_random[matrix_random > 25])

print("sum", np.sum(matrix_random))
print("sum", np.mean(matrix_random))
print("sum", np.std(matrix_random))
