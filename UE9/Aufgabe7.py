import numpy as np
import random


def solve_u(U, b):
    x = []
    for i in range(b.shape[0])[::-1]:
        weighted_sum = sum(
            [
                x[b.shape[0]-1-j] * U[i, j] for j in range(i+1, b.shape[0])[::-1]
            ]
        )
        x.append(
            (b[i] - weighted_sum) / U[i, i]
        )
    return np.array(x[::-1])


def gen_random_expression():
    dim = random.randint(1, 10)
    U = np.zeros((dim, dim))
    for x in range(dim):
        for y in range(dim):
            if x <= y:
                U[x, y] = random.randint(1, 1000)
    b = np.array([random.randint(1, 100) for _ in range(dim)])
    return U, b


if __name__ == '__main__':
    U = np.array([[1, 2, 3],
                  [0, 4, 5],
                  [0, 0, 6]])
    b = np.array([1, 2, 3])

    print(solve_u(U, b))
    print(np.linalg.inv(U)@b)

    U = np.array([[7, 10, 2],
                  [0, 24, 1],
                  [0, 0, 3]])
    b = np.array([1, 1, 1])

    print(solve_u(U, b))
    print(np.linalg.inv(U) @ b)

    for _ in range(int(input('Number of random samples: '))):
        U, b = gen_random_expression()
        print('\n', solve_u(U, b))
        print(np.linalg.inv(U) @ b)

