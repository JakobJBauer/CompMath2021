import numpy as np


def is_hermitian(matrix):
    matrix = np.matrix(matrix)
    return np.array_equal(matrix, matrix.H)


if __name__ == '__main__':
    hermitian = np.array([[0, 1 - 3j, 7 + 22j],
                          [1 + 3j, 13, 12 - 8j],
                          [7 - 22j, 12 + 8j, 1]])

    non_hermitian = [[12, 41 + 23j, 43],
                     [9 + 7j, 0 - 12j, 3 - 5j],
                     [3, 4, 1]]
    print(is_hermitian(hermitian))
    print(is_hermitian(non_hermitian))
