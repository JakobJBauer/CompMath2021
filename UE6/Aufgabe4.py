import random


def get_sequence(n: int) -> list[int, ...]:
    output = []
    while n > 0 and not output[-31:-1] == [4, 2, 1]*10:
        output.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return output


def is_verified_sequence(sequence: list[int, ...]) -> bool:
    return sequence[-16:-1] == [4, 2, 1] * 5


print('Problem 4, A')
for i in range(20):
    sequence = get_sequence(random.randint(0, 999999))
    print('\n', sequence)
    print('Verified: ', is_verified_sequence(sequence))
