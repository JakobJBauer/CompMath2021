import numpy as np

n = 5

matrix = np.zeros((n, n))
np.fill_diagonal(matrix, 1)
matrix = np.rot90(matrix)
matrix[:, -1] = 1
matrix[0, :] = 1

print(matrix)
