def get_me_1() -> str:
    d = {'key1': [1, 2, {'key2': ['do not get confused', {'tough': [1, 2, [['get me']]]}]}]}
    return d['key1'][2]['key2'][1]['tough'][2][0][0]


def get_me_2() -> str:
    d = {'key2': [1, [[], {'bug': {'bug': 'get me'}}]]}
    return d['key2'][1][1]['bug']['bug']


def reverse_keys(d: dict) -> dict:
    output: dict = {}
    for key, value in d.items():
        output[key[::-1]] = value
    return output


print('Problem 7, A')
print(get_me_1())
print(get_me_2())

print('\nProblem 7, B')
d = {'reverse_me': 'DONT', 'reverse_me_too': 'STOP IT', 'this is reversed': True}
print('Dict: ', d)
print('Reversed: ', reverse_keys(d))
