def count(fun):
    counter = 0

    def inner():
        fun()
        nonlocal counter
        counter += 1
        print(fun.__name__, 'was called ', counter, ' time(s)')
        return counter
    return inner


@count
def f():
    print('F was called')


@count
def g():
    print('G was called')


print('Problem A')
print(f())
print('\n')
print(f())
print('\n')
print(f())
print('\n')
print(f())
print('\n')
print(g())
print('\n')
print(f())
