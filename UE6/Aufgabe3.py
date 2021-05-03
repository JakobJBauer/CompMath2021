def contains_duplicate(list_input: list[int, ...]) -> bool:
    counter_dict: dict = {}
    for value in list_input:
        if counter_dict.get(value, 0) == 1:
            return True
        counter_dict[value] = 1
    return False


def order_string(string_input: str) -> str:     # insertion sort
    li = list(string_input)
    for i in range(1, len(li)):
        pivot = li[i]
        j = i - 1
        while li[j] > pivot and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = pivot
    return str(li)


def remove_duplicates(li: list) -> list:
    counter_dict: dict = {}
    removed_elements = []
    i = 0
    while i < len(li):
        if counter_dict.get(li[i], 0) == 1:
            removed_elements.append(li.pop(i))
        else:
            counter_dict[li[i]] = 1
            i += 1
    return removed_elements


def contains_sublist(li: list) -> bool:
    for el in li:
        if type(el) == list:
            return True
    return False


def concat_by_range(li: list, n: int) -> list:
    output = []
    for el in li:
        for i in range(n):
            output.append(str(el) + str(i+1))
    return output


print('Problem 3, A')
print(contains_duplicate([1, 2, 3]))
print(contains_duplicate([1, 2, 3, 1]))

print('\nProblem 3, B')
print(order_string('eHllo'))
print(order_string('dcabfehgkjimonlpsqtrvuwzxy'))

print('\nProblem 3, C')
buffer = [1, 2, 3, 1, 2, 3, 2, 2]
print(remove_duplicates(buffer))    # should be [1, 2, 3, 2, 2]
print(buffer)   # should be [1, 2, 3]
print(remove_duplicates([1, 2, 3]))    # should be []
print(remove_duplicates(['one', 'two', 'lol', 'foo', 'two', 'foo']))    # should be ['two', 'foo']

print('\nProblem 3, D')
print(contains_sublist([1, 2, 3]))      # False
print(contains_sublist([1, 2, 3, [1, 2]]))      # True
print(contains_sublist([1, 2, 3, []]))      # True

print('\nProblem 3, E')
print(concat_by_range(['h', 'a'], 5))
print(concat_by_range(['h', 2], 2))
print(concat_by_range([True, False], 2))
