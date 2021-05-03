from collections import OrderedDict


def insert_front(ordered_dict: OrderedDict, element: dict) -> None:
    el_key = next(iter(element))
    ordered_dict[el_key] = element[el_key]
    ordered_dict.move_to_end(el_key, last=False)


print('Problem A')
t_dict = OrderedDict(a=12, b=152)
el = {'c': 1}
print('dict: ', dict(t_dict))
insert_front(t_dict, el)
print('inserted: ', dict(t_dict))
