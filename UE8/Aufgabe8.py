import numpy as np

n = 10
assert n % 2 == 0
matrix = np.zeros((n, n), dtype=np.int8)

range = np.arange(0, n, 2)
matrix[range, range] = 1
matrix[range + 1, range] = 1
matrix[range, range + 1] = 1
matrix[range + 1, range + 1] = 1

print(matrix)