from collections import OrderedDict


def insert_front(ordered_dict: OrderedDict, element: dict) -> None:
    el_key = next(iter(element))
    ordered_dict[el_key] = element[el_key]
    ordered_dict.move_to_end(el_key, last=False)


def get_common_elements(li1: list, li2: list) -> list:
    return list(filter(lambda x: x in li2, li1))


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
