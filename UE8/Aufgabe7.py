import numpy as np


def norm(matrix, p):
    return sum(sum(matrix[:, :]**p))**(1/p)


x = 5
mat = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print(norm(mat, x))
