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
    output = l[0]
    for function in l[1:]:
        output = output(function)

    def comp_inner(x):
        return output(x)
    return comp_inner


print(straight())
print(sinus())

cum_func = comp([math.sin, math.cos, math.sqrt, math.tan])
print(cum_func)

