from collections import OrderedDict


def insert_front(ordered_dict: OrderedDict, element: dict) -> None:
    el_key = next(iter(element))
    ordered_dict[el_key] = element[el_key]
    ordered_dict.move_to_end(el_key, last=False)


def get_common_elements(li1: list, li2: list) -> list:
    return list(filter(lambda x: x in li2, li1))


def dict2lists(di: dict) -> list:
    return [[key] + [item for item in values] for key, values in di.items()]


def invert_dict_deprecated(di: dict) -> dict:
    """DEPRECATED
    Inverts dictionary if it has less than or two layers"""
    outp = {}
    for key, value in di.items():
        if not value:
            outp[key] = value
        else:
            outp[next(iter(value))] = invert_dict({key: value[next(iter(value))]})
    return outp


def dict2keylist(di: dict) -> list:
    """Transforms a given dictionary to a list of its keys"""
    if not di:
        return []
    key = next(iter(di))
    value = di.get(key)
    return [key] + dict2keylist(value)


def keylist2dict(li: list) -> dict:
    """Transforms a given list of keys to a dictionary"""
    return {li.pop(0): keylist2dict(li)} if li else {}


def invert_dict(di: dict) -> dict:
    output = {}
    for key in di:
        output.update(keylist2dict(list(reversed(dict2keylist({key: di[key]})))))
    return output

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

test_dict = {'a': {'b': {}}}
print('Dict2Keys ', dict2keylist(test_dict))
test_dict = {'a1': {'b1': {}}, 'a2': {'b2': {}}}
print('Dict2Keys ', dict2keylist(test_dict))
test_dict = {'a': {'b1': {}, 'b2': {}}}     # This structure is impossible, handling is: take first key (unordered)
print('Dict2Keys ', dict2keylist(test_dict))

test_list = ['a', 'b', 'c']
print('\nList2Dict: ', keylist2dict(test_list))
test_list = ['a1', 'b2', 'c3']
print('List2Dict: ', keylist2dict(test_list))
test_list = ['a', 'b', 'g', 'j']
print('List2Dict: ', keylist2dict(test_list))

test_dict = {'a': {'b': {}}}
print('\nInverseDict ', invert_dict(test_dict))
test_dict = {'a1': {'b1': {}}, 'a2': {'b2': {}}}
print('InverseDict ', invert_dict(test_dict))
test_dict = {'a': {'b1': {}, 'b2': {}}}     # This structure is impossible, handling is: take first key (unordered)
print('InverseDict ', invert_dict(test_dict))
test_dict = {'a': {'b': {'c': {'d': {}, 'e': {}, 'f': {}}}}, 'g': {'h': {}, 'i': {'j': {}}}, 'k': {'l': {}}}
print('InverseDict ', invert_dict(test_dict))
