import numpy as np

n = 5

matrix = np.zeros((n, n), dtype=np.int8)
np.fill_diagonal(matrix, 1)
matrix = np.rot90(matrix)
matrix[:, -1] = 1
matrix[0, :] = 1

print(matrix)

range = np.arange(n)
matrix2 = np.zeros((n, n), dtype=np.int8)

matrix2[n - 1 - range, range] = 1
matrix2[:, -1] = 1
matrix2[0, :] = 1

print()
print(matrix2)
