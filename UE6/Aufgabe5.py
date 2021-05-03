import random


def validate_fermats_problem(a: int, b: int, c: int, n: int) -> bool:
    assert n > 2
    assert a >= 1
    assert b >= 1
    assert c >= 1
    return not a**n + b**n == c**n


def nice_sequence(n: float, ny: float = None) -> (float, float):
    if ny is None:
        ny = n
    next_nx = (2 * n**3)/(3 * n**2 - 1)
    next_ny = (1/2) * (ny + 1/ny)
    if next_nx == n and next_ny == ny:
        return n, ny
    return nice_sequence(next_nx, next_ny)


print('Problem 5, A')
for i in range(200):
    print('Fermat holds: ', validate_fermats_problem(
        random.randint(1, 99999),
        random.randint(1, 99999),
        random.randint(1, 99999),
        random.randint(3, 99999))
    )

print('\nProblem 5, B')
x, y = nice_sequence(50000)
print('X: ', x, 'Y: ', y)
