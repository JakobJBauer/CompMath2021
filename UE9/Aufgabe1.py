import numpy as np


def square(num):
    matrix = np.zeros((num, num), dtype=np.int8)
    matrix[:, 0] = 1
    matrix[0, :] = 1
    matrix[:, -1] = 1
    matrix[-1, :] = 1
    return matrix


def line(num):
    matrix = np.zeros((num, num), dtype=np.int8)
    matrix[:, (num-1)//2] = 1
    return matrix


def snake(num):
    matrix = np.zeros((num, num), dtype=np.int8)
    matrix[0, :] = 1
    matrix[-1, :] = 1
    matrix[(num-1)//2, :] = 1
    matrix[np.arange(0, (num-1)//2), -1] = 1
    matrix[np.arange((num-1)//2, num-1), 0] = 1
    return matrix


if __name__ == "__main__":
    n = int(input('n: '))
    if n % 2 == 0:
        raise ValueError("n must be odd")

    print(square(n))
    print('\n', line(n))
    print('\n', snake(n))