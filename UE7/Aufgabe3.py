class Vector:
    @staticmethod
    def add(z1: list, z2: list):
        if len(z1) != len(z2):
            raise ValueError("z1 and z2 need to have the same dimension")
        return [z1[i] + z2[i] for i in range(len(z1))]

    @staticmethod
    def scalar(a: float, z1: list):
        return [a * z_dim for z_dim in z1]


class VectorPlus(Vector):  # BillaPlus
    @staticmethod
    def vector_prod(z1: list, z2: list):
        if len(z1) != len(z2):
            raise ValueError("z1 and z2 need to have the same dimension")
        return [z1[(i + 1) % len(z1)] * z2[(i + 2) % len(z2)] - z2[(i + 1) % len(z2)] * z1[(i + 2) % len(z1)] for i in range(len(z1))]

    @staticmethod
    def tensor(z1: list, z2: list):
        return [[z1_el * z2_el for z2_el in z2] for z1_el in z1]


print(Vector.add([1, 2, 3, 4], [5, 6, 7, 8]))
print(Vector.scalar(4.3, [5, 6, 7, 8]))
print(VectorPlus.vector_prod([1, 2, 3], [3, 4, 5]))
print(VectorPlus.tensor([1, 2, 3], [3, 4, 5]))
