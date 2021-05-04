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

