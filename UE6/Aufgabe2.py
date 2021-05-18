def odd(n: int) -> int:
    if type(n) != int:
        raise TypeError('n is not an Integer')
    number_of_odd_digits = 0
    for digit in str(n):
        if int(digit) % 2 == 1:
            number_of_odd_digits += 1
    return number_of_odd_digits


def even(n: int) -> int:
    if type(n) != int:
        raise TypeError
    number_of_even_digits = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            number_of_even_digits += 1
    return number_of_even_digits


def odd_floats(n: float) -> int:
    if type(n) != float:
        raise TypeError('n is not a float number')
    split_number: list[str, str] = str(n).split('.')
    # digits pre decimal point
    number_of_odd_digits = odd(int(split_number[0]))
    # digits post decimal point
    number_of_odd_digits += odd(int(split_number[1]))
    return number_of_odd_digits


def even_floats(n: float) -> int:
    if type(n) != float:
        raise TypeError('n is not a float number')
    split_number: list[str, str] = str(n).split('.')
    # digits pre decimal point
    number_of_even_digits = even(int(split_number[0]))
    # digits post decimal point, only the first 10
    number_of_even_digits += even(int(split_number[1][:9]))
    return number_of_even_digits


def count_prime_digits(n: int) -> int:
    return sum([is_prime(int(digit)) for digit in str(n)])
    # output = 0
    # for digit in str(n):
    #     if is_prime(int(digit)):
    #         output += 1
    # return output


def is_prime(n: int) -> bool:
    # only works for single digits
    return n == 1 or n == 2 or n == 3 or n == 5 or n == 7


print('Problem 2, A')
print('Odd: ', odd(19998))
print('Even: ', even(19998))

print('\nProblem 2, B')
print('Odd: ', odd_floats(5.000))      # should be 9
print('Odd: ', odd_floats(19998.89236421))      # should be 8
print('Even: ', even_floats(5.000))    # should be 7
print('Even: ', even_floats(19998.89236421))    # should be 6

print('\nProblem 2, C')
print(count_prime_digits(1234567890))   # should be 5
print(count_prime_digits(986469))   # should be 0
print(count_prime_digits(111111))   # should be 6

