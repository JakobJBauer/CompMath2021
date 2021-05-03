import pdb
from math import sin


def f(x):
    pdb.set_trace()
    x = x + 1.0
    return sin(x) ** 2 + x


print(" value of f(x)", f(1))
