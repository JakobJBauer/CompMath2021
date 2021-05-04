def midpointrule(a, b, f, n) -> list:
    output_vector = []
    k_list = range(n+1)
    for k in k_list:
        N = 2**k
        j_list = range(N+1)
        intervals = [a + j * ((b - a) / N)for j in j_list]

        for xn in intervals:
            output_vector.append((b - a)/N * sum([f((xn[j-1] + xn[j])/2) for j in range(1, N+1)]))
    return output_vector
