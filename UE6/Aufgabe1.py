def convert_to_integer(tuple_input):
    return sum([tuple_input[-1-i] * 10 ** i for i in range(len(tuple_input) - 1, -1, -1)])
    # output = ""
    # for number in tuple_input:
    #     output += str(number)
    # return int(output)


def add_tuples(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple:
    return tuple([tuple1[i] + tuple2[i] for i in range(len(tuple1))])
    # output: list = []
    # for i in range(len(tuple1)):
    #     output.append(tuple1[i] + tuple2[i])
    # return tuple(output)


def add_list_of_tuples(list_of_tuples: list[tuple[int, ...], ...]) -> list:
    return [sum(tuple_attr) for tuple_attr in list_of_tuples]
    # output = []
    # for tuple_attr in list_of_tuples:
    #     buffer: int = 0
    #     for number in tuple_attr:
    #         buffer += number
    #     output.append(buffer)
    # return output


def string_to_tuple(string_input: str) -> tuple[str, ...]:
    return tuple([x for x in string_input])
    # output: list = []
    # for character in string_input:
    #     output.append(character)
    # return tuple(output)


print('Problem 1, A')
print(convert_to_integer((1, 2, 3)))

print('\nProblem 1, B')
print(add_tuples((1, 2, 3), (3, 2, 1)))

print('\nProblem 1, C')
print(add_list_of_tuples([(1, 2), (2, 3), (3, 4)]))

print('\nProblem 1, D')
print(string_to_tuple('python3.9'))
