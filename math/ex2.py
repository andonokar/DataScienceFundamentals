import numpy as np

matrix = np.array([[1, 2], [3, 4]])
det = np.linalg.det(matrix)
print(f"The determinant of the matrix is {det}")

inverse = np.linalg.inv(matrix)
print(f"The inverse of the matrix is:\n{inverse}")

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f"The eigenvalues of the matrix are:\n{eigenvalues}")
print(f"The eigenvectors of the matrix are:\n{eigenvectors}")

u, s, vh = np.linalg.svd(matrix)
print(f"The singular values of the matrix are:\n{s}")
print(f"The left singular vectors (U) of the matrix are:\n{u}")
print(f"The right singular vectors (Vh) of the matrix are:\n{vh}")

reconstructed_matrix = u @ np.diag(s) @ vh
print(f"The reconstructed matrix is:\n{reconstructed_matrix}")


