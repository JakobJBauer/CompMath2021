import random
import numpy as np
import scipy.linalg


def invert_l(matrix):
    if matrix.shape[0] <= 1:
        return np.array([[1/matrix[0, 0]]])
    p = matrix.shape[0] // 2            # floor
    L11 = matrix[:p, :p]                # upper left
    L21 = matrix[p:, :p]                # lower left
    L22 = matrix[p:, p:]                # lower right

    zero = np.zeros((p, matrix.shape[0] - p))
    return np.block([[invert_l(L11), zero],
                     [-invert_l(L22) @ L21 @ invert_l(L11), invert_l(L22)]])


def gen_random_matrix():
    dim = random.randint(1, 10)
    M = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            if i >= j:
                M[i, j] = random.randint(1, 1000)
            else:
                M[i, j] = 0
    return M


if __name__ == '__main__':
    U = np.array([
        [ 2,  0,  0,  0,  0],
        [ 5,  2,  0,  0,  0],
        [22, 30,  2,  0,  0],
        [42,  9,  2, 43,  0],
        [ 3, 89, 32,  5, 31]
    ])

    print(U, '\n')
    # a)
    print('holds a: ', abs(np.linalg.det(U) - np.prod([U[j, j] for j in range(U.shape[0])])) < 10e-6, '\n')
    print(invert_l(U).astype(int), '\n')
    print(np.array(scipy.linalg.inv(U)).astype(int), '\n')  # b) seems to be true

    for _ in range(int(input('Number of random samples: '))):
        U = gen_random_matrix()
        print(U, '\n')
        # a)
        print('holds a: ', abs(np.linalg.det(U) - np.prod([U[j, j] for j in range(U.shape[0])])) < 10e-6, '\n')
        print(invert_l(U).astype(int), '\n')
        print(np.array(scipy.linalg.inv(U)).astype(int), '\n')
