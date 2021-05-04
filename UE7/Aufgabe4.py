import math


def dec(ev):
    def dec_inner(fun):
        def evaluate_fun():
            return fun(ev)
        return evaluate_fun
    return dec_inner


@dec(12)
def straight(x):
    return 12*x+24


@dec(1)
def sinus(x):
    return math.sin(x)


def comp(l: list):
    def inner(x):
        output = l[0](x)
        for function in l[1:]:
            output = function(output)
        return output
    return inner


print('Problem A')
print(straight())
print(sinus())

print('\n\nProblem B')
print('\nRollercoaster:')
cum_func = comp([math.sin, math.cos, math.sqrt, math.tan])
print(cum_func)
print(cum_func(12))
print(cum_func(120))
print(cum_func(1200))

print('\nReal big:')
cum_func2 = comp([math.exp, math.floor])
print(cum_func2)
print(cum_func2(20))
print(cum_func2(200))

