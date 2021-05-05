def do_crazy_string_stuff(s1: str, s2: str) -> str:
    print((s1 + s2)[::-1])
    return (s1 + s2)[::-1]


def flipperino(s:str) -> str:
    s = s.split(' ')
    s[0], s[-1] = s[-1], s[0]
    s = ' '.join(s)
    return do_crazy_string_stuff(s, '')


def create_nice_output() -> None:
    for i in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(i, i**2, i**3))


print('Problem 6, A')
do_crazy_string_stuff('Hello', 'Dude')
do_crazy_string_stuff('Ich bin ein geteilter', 'Satz bruder')

print('\nProblem 6, B')
flipperino('PARKOUR, wohooo this is just crazy')
flipperino('Become great in python you must!')

print('\nProblem 6, C')
create_nice_output()
