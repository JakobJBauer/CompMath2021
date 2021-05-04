from collections import OrderedDict


def insert_front(ordered_dict: OrderedDict, element: dict) -> None:
    el_key = next(iter(element))
    ordered_dict[el_key] = element[el_key]
    ordered_dict.move_to_end(el_key, last=False)


def get_common_elements(li1: list, li2: list) -> list:
    return list(filter(lambda x: x in li2, li1))


def dict2lists(di: dict) -> list:
    return [[key] + [item for item in values] for key, values in di.items()]


def inverse_dict(di: dict) -> dict:
    out = {}
    for key, value in di.items():
        if value is not {}:
            x = next(iter(value))
            out[x] = inverse_dict({key: di[key]})
    return out


print('Problem A')
t_dict = OrderedDict(a=12, b=152)
el = {'c': 1}
print('dict: ', dict(t_dict))
insert_front(t_dict, el)
print('inserted: ', dict(t_dict))

print('\nProblem B')
l1 = [1, 5, 5]
l2 = [3, 4, 5, 5, 10]
l3 = [5, 5, 10, 20]
print(get_common_elements(get_common_elements(l1, l2), l3))

print('\nProblem C')
inp = {'gfg': [1, 3, 5], 'is': [7, 6], 'best': [4, 5]}
print(dict2lists(inp))

print('\nProblem D')
test_dict = {'a': {'b': {}}, 'd': {'e': {}}, 'f': {'g': {}}}
print('Initial: ', test_dict)
test_dict = inverse_dict(test_dict)
print('Reversed: ', test_dict)
