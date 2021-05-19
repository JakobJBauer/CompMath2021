import numpy as np

n = 5
matrix = np.zeros((n, n), dtype=np.int8)
np.fill_diagonal(matrix, 1)
matrix = np.fliplr(matrix)
np.fill_diagonal(matrix, 1)

print(matrix)
