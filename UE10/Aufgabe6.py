from functools import reduce
import numpy as np


def save_matrix(matrix):
    with open('matrix.dat', 'w') as f:
        f.write('[\n')
        for line in matrix:
            f.write(f"[{reduce(lambda x,y: str(x) + ', ' + str(y), line)}]\n")
        f.write(']')


def load_matrix(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')[1:-1]
        dim = len(lines)

        matrix = np.zeros((dim, dim))

        for y in range(dim):
            values = lines[y][1:-1].split(', ')
            for x in range(dim):
                matrix[y, x] = float(values[x])

        return matrix


if __name__ == '__main__':
    m = np.array([[1., 2., 3.], [2., 3., 4.], [3., 4., 5.]])
    save_matrix(m)
    m2 = load_matrix('matrix.dat')

    np.savetxt('matrix_np.dat', m)
    m_np = np.loadtxt('matrix_np.dat')
    print(m, '\n\n', m2)
    print('\n', m_np)
