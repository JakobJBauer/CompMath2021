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


print('A')
a, b, f, n = 1, 5, math.sin, 5
print('Input: ', a, b, f, n, '\nOutput:', midpointrule(a, b, f, n))
