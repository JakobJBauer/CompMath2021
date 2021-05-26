import numpy as np


def trim(v):
    """cuts lowest abs. and highest imag. value out of v"""
    i = np.argmin(np.abs(v))
    v = np.delete(v, i)
    i = np.argmax(np.imag(v))
    v = np.delete(v, i)
    return v


if __name__ == '__main__':
    x = np.array([54, -2+4j, -2+5j, 2+1j, 2+2j, 2+3j])
    print(trim(x))
    x = np.array([2+1j, -2+2j, 5, -5.5, 0+44j, 0+45j])
    print(trim(x))
