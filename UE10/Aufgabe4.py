import numpy as np


def newton(f, fprime, x0, tau):
    sequence = []
    xk1 = x0

    while True:
        sequence.append(xk1)

        if abs(fprime(xk1) <= tau):
            print('Warning!')
            return xk1, sequence

        cmp_value = tau if abs(xk1) <= tau else tau * abs(xk1)
        if abs(f(xk1)) <= tau and abs(xk1 - xk0) <= cmp_value:
            return xk1, sequence

        xk0 = xk1                           # for the next iteration, set values
        xk1 = xk0 - f(xk0)/fprime(xk0)


if __name__ == '__main__':
    print(newton(lambda x: x**2 + np.exp(x) - 2, lambda x: 2*x + np.exp(x), 4, 10e-12))
