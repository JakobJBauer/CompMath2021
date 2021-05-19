from UE8 import Aufgabe3


class VectorComplex(Aufgabe3.Vector):
    def __init__(self, real, complex_):
        if len(real) != len(complex_):
            raise ValueError(f'Dimensions {len(real)} and {len(complex_)} do not match')
        super().__init__(real)
        self.__complex_part = complex_

    @property
    def real_part(self):
        return self.vector

    @property
    def complex_part(self):
        return self.__complex_part

    def __len__(self):
        return len(self.real_part)

    def __add__(self, other: 'VectorComplex'):
        return VectorComplex(
            [x + y for x, y in zip(self.real_part, other.real_part)],
            [x + y for x, y in zip(self.complex_part, other.complex_part)]
        )

    def __sub__(self, other: 'VectorComplex'):
        return VectorComplex(
            [x - y for x, y in zip(self.real_part, other.real_part)],
            [x - y for x, y in zip(self.complex_part, other.complex_part)]
        )

    def sum(self):
        return sum(self.real_part), sum(self.complex_part)

    def norm(self, p):
        return sum(map(lambda x: (x[0]**2 + x[1]**2)**p, zip(self.real_part, self.complex_part)))**(1/p)


a = VectorComplex([1, 2, 3, 4, 5], [1, 1, 1, 1, 1])
b = VectorComplex([2, 3, 4], [4, 5, 5])
c = VectorComplex([1, 2, 3], [0, 0, 0])

print()
print('c + b:', (c+b).sum())
print('c - b:', (c-b).sum())
print('sum of a:', a.sum())
print('ncount of a:', a.ncount())
print('norm of a, grade 2:', a.norm(2))
print('norm of a, grade 4:', a.norm(4))
