import numpy as np


def get_max_from_range(upperbound, vector):
    return vector[:upperbound-1][abs(vector[:upperbound-1]).argmax()]


def set_upper_boundary(value, vector):
    vector[vector > value] = value


if __name__ == '__main__':
    upperb = int(input('Upperbound: '))
    dim = np.random.randint(1000)
    vect = np.random.rand(dim) * upperb * 2 + np.random.random(dim) * upperb * 2j
    print(vect)
    maxval = get_max_from_range(upperb, vect)
    print('\n', maxval)
    set_upper_boundary(maxval, vect)
    print('\n', vect)
