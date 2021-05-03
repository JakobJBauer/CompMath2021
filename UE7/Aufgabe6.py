# copy from Task 2
from typing import Tuple


class Complex:
    """This class allows to add, multiply and divide two complex numbers"""
    def __init__(self, z1: Tuple[float, float], z2: Tuple[float, float]) -> None:
        self.z1 = z1
        self.z2 = z2

    def add(self) -> Tuple[float, float]:
        return self.z1[0] + self.z2[0], self.z1[1] + self.z2[1]

    def multiply(self) -> Tuple[float, float]:
        return self.z1[0] * self.z2[0], self.z1[1] * self.z2[1]

    def divide(self) -> Tuple[float, float]:
        return self.z1[0] / self.z2[0], self.z1[1] / self.z2[1]
# end copy


# copy from Task 3
class Vector:
    """This class contains two basic Vectorfunctions, which can be statically accessed

    Function add takes two Vectors and returns the sum of them

    Function scalar takes a float number and a Vector and multiplies every Dimension of the Vector with the scalar. The
    product is returned"""
    @staticmethod
    def add(z1: list, z2: list):
        if len(z1) != len(z2):
            raise ValueError("z1 and z2 need to have the same dimension")
        return [z1[i] + z2[i] for i in range(len(z1))]

    @staticmethod
    def scalar(a: float, z1: list):
        return [a * z_dim for z_dim in z1]


class VectorPlus(Vector):  # BillaPlus
    """This class contains two extendes Vectorfunctions, which can be statically accessed.

    Function vector_prod takes two Vectors and returns the crossproduct of them

    Function tensor takes two Vectors and returns the tensor product of them"""
    @staticmethod
    def vector_prod(z1: list, z2: list):
        if len(z1) != len(z2):
            raise ValueError("z1 and z2 need to have the same dimension")
        return [z1[(i + 1) % len(z1)] * z2[(i + 2) % len(z2)] - z2[(i + 1) % len(z2)] * z1[(i + 2) % len(z1)] for i in range(len(z1))]

    @staticmethod
    def tensor(z1: list, z2: list):
        return [[z1_el * z2_el for z2_el in z2] for z1_el in z1]
# end copy


print('Problem A')

print('\n\n\n', Complex.__doc__)
print('\n\n\n', Vector.__doc__)
print('\n\n\n', VectorPlus.__doc__)
