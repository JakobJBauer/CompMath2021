import numpy as np


# def power_iteration(A, tau, x):
#     if not np.array_equal(A, A.T):
#         raise ValueError('A is not symmetric')
#     return seq(A, tau, x, x*A@x)
#
# def seq(A, tau, x, lamb):
#     next_x = A@x / np.linalg.norm(A@x)
#     next_lamb = next_x @ (A@next_x)
#     if np.linalg.norm(A@next_x - next_lamb*next_x) <= tau:
#         if np.abs(next_lamb) <= tau:
#             if np.abs(lamb - next_lamb) <= tau:
#                 return next_lamb, next_x
#         if np.abs(lamb - next_lamb) <= tau * np.abs(next_lamb):
#             return next_lamb, next_x
#     return seq(A, tau, next_x, next_lamb)

def power_iteration(A, tol, x):
    if not np.array_equal(A, A.T):
        raise Exception("A is not symmetric")

    next_lam = 0
    while True:
        x = (A@x)/np.linalg.norm(A@x)
        lam = next_lam
        next_lam = x @ (A @ x)
        if np.linalg.norm(A @ x - next_lam * x) <= tol:
            if np.abs(next_lam) <= tol:
                if np.abs(lam - next_lam) <= tol:
                    return next_lam, x
            if np.abs(lam - next_lam) <= tol * np.abs(next_lam):
                return next_lam, x


if __name__ == '__main__':
    # error
    # A = np.array([[1,2], [3,1]])
    # x0 = np.array([2,3])
    # print('poweriteration:\n', power_iteration(A, 10e-12, x0))

    A = np.array([[3,0,0],
                  [0,1,0],
                  [0,0,3]])
    x0 = np.array([1,1,1])

    print('poweriteration:\n', power_iteration(A, 10e-12, x0))
    print('\n\n', 'comparison:\n', np.linalg.eig(A)[0])
    print('\n\n', "corresponding eigenvectors:\n", np.linalg.eig(A)[1])

