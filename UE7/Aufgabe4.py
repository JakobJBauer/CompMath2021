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


def comp(*args):
    def wrapper(f):
        def inner(x):
            output = f(x)
            for function in args:
                output = function(output)
            return output
        return inner
    return wrapper


@comp(math.sin, math.tan)
def sqrt(x):
    return math.sqrt(x)


@comp(math.sqrt)
def linear(x):
    return x


print('Problem A')
print(straight())
print(sinus())

print('\n\nProblem B')
print('\nRollercoaster:')
cum_func = comp(math.sin, math.cos, math.sqrt, math.tan)
print(cum_func)
print(cum_func(12))
print(cum_func(120))
print(cum_func(1200))

print('\nReal big:')
cum_func2 = comp(math.exp, math.floor)
print(cum_func2)
print(cum_func2(20))
print(cum_func2(200))

print('\nWeird region')
print(sqrt(25))
print(linear(25))

