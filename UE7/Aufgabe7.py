def invert_dict(di: dict) -> dict:
    """Inverts dictionary if it has less than or two layers"""
    outp = {}
    for key, value in di.items():
        if value == {}:
            outp[key] = value
        else:
            outp[next(iter(value))] = invert_dict({key: value[next(iter(value))]})
    return outp


def invert_dict_multilayer(di:dict) -> dict:
    """Inverts dictionary even with multiple layers"""
    # ToDO: Nothing works here dude
    outp = {}
    for key, value in di.items():
        if value == {}:
            outp[key] = value
        else:
            outp = swap_keys(invert_dict_multilayer(value))
    return outp


def swap_keys(di: dict) -> dict:
    outp = {}
    for key, value in di.items():
        if value == {}:
            outp[key] = value
        else:
            outp[next(iter(value))] = {key: value[next(iter(value))]}
    return outp


test_dict = {'a': {'b': {}}}
print('Swap keys', swap_keys(test_dict))
test_dict = {'a1': {'b1': {}}, 'a2': {'b2': {}}}
print('Swap keys', swap_keys(test_dict))
test_dict = {'a': {'b1': {}, 'b2': {}}}     # This structure is impossible, handling is: take first key (unordered)
print('Swap keys', swap_keys(test_dict))

test_dict = {'a': {'b': {}}, 'd': {'e': {}}, 'f': {'g': {}}}
print('\nInvert dict: ', invert_dict(test_dict))
print('Invert dict multilayer: ', invert_dict_multilayer(test_dict))

test_dict = {'a': {'b': {'c': {'d': {}, 'e': {}, 'f': {}}}}, 'g': {'h': {}, 'i': {'j': {}}}, 'k': {'l': {}}}
print('\nInvert dict: ', invert_dict(test_dict))
print('Invert dict multilayer: ', invert_dict_multilayer(test_dict))
