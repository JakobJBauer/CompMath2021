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

def poweriteration(A, tol, x):
    if not np.array_equal(A, A.T):
        raise Exception("matrix has to be symmetric")
    else:
        l = 0
        while True:
            x = (A@x)/np.linalg.norm(A@x)
            l_past = l
            l = x@(A@x)
            if np.linalg.norm(A @ x - l*x) <= tol:
                if(np.abs(l) <= tol):
                    if np.abs(l_past - l) <= tol:
                        return (l, x)
                elif np.abs(l_past - l) <= tol * np.abs(l):
                    return (l, x)


if __name__ == '__main__':
    A = np.array([[3,4,5],
                  [4,2,7],
                  [5,7,9]])
    x0 = np.array([2,3,4])

    print('poweriteration:\n', poweriteration(A, 10e-12, x0))
    print('\n\n', 'comparison:\n', np.linalg.eig(A)[0])
    print('\n\n', "corresponding eigenvectors:\n", np.linalg.eig(A)[1])

