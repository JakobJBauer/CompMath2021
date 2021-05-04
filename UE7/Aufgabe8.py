import math


def midpointrule(a, b, f, n) -> list:
    output_vector = []
    k_list = range(n+1)
    for k in k_list:
        N = 2**k
        j_list = range(N+1)
        intervals = [a + j * ((b - a) / N) for j in j_list]

        for _ in intervals:
            output_vector.append((b - a)/N * sum([f((intervals[j-1] + intervals[j])/2) for j in range(1, N+1)]))
    return output_vector


a, b, f, n = -5, 5, lambda x: x**2, 10
result = midpointrule(a, b, f, n)
print('\nInput: ', a, b, f, n, '\nOutput:', result, '\nLast element: ', result[-1], '\n')

a, b, f, n = -1, 1, lambda x: math.exp(x), 10
result = midpointrule(a, b, f, n)
print('\nInput: ', a, b, f, n, '\nOutput:', result, '\nLast element: ', result[-1], '\n')

a, b, f, n = -1, 1, lambda x: 5*x, 10
result = midpointrule(a, b, f, n)
print('\nInput: ', a, b, f, n, '\nOutput:', result, '\nLast element: ', result[-1], '\n')

a, b, f, n = -1, 1, lambda x: -5*x, 10
result = midpointrule(a, b, f, n)
print('\nInput: ', a, b, f, n, '\nOutput:', result, '\nLast element: ', result[-1], '\n')

a, b, f, n = -1, 1, lambda x: 5, 10
result = midpointrule(a, b, f, n)
print('\nInput: ', a, b, f, n, '\nOutput:', result, '\nLast element: ', result[-1], '\n')

