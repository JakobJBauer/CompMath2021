class Vector:
    def __init__(self, vector: list):
        self.vector = vector

    def __len__(self):
        return len(self.vector)

    def __iter__(self):
        return iter(self.vector)

    def __add__(self, other):
        if len(self.vector) != len(other):
            raise ValueError(f'Dimensions {len(self.vector)} and {len(other)} do not match')
        return Vector([x + y for x, y in zip(self.vector, other)])

    def __sub__(self, other):
        if len(self.vector) != len(other):
            raise ValueError(f'Dimensions {len(self.vector)} and {len(other)} do not match')
        return Vector([x - y for x, y in zip(self.vector, other)])

    def norm(self, p):
        return sum(map(lambda x: x**p, self.vector))**(1/p)

    def sum(self):
        return sum(self.vector)

    def ncount(self):
        return len(self)


if __name__ == '__main__':
    a = Vector([1, 2, 3, 4])
    b = Vector([2, 3, 4, 5])
    print('a + b:', (a+b).sum())
    print('a - b:', (a-b).sum())
    print('sum of a:', a.sum())
    print('ncount of a:', a.ncount())
    print('norm of a, grade 2:', a.norm(2))
    print('norm of a, grade 4:', a.norm(4))
