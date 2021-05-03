import pdb
from math import sin


print("This is a debugging test.")


def f(x):
    pdb.set_trace()
    x = x + 1.0
    return sin(x) ** 2 + x


print(" value of f(x)", f(1))


print('Problem 8, A')
print('It starts the python debugger at the line with set_trace(), from where you can further debug the program')

print('Problem 8, B')
print('n(ext): step into the next line of code')
print('s(tep): step into the next function/operation')
print('l(ist): prints the 11 lines around the current statement')
print('c(ont(inue)): Continue execution, only stop when a breakpoint is encountered.')
