from typing import Tuple


class Complex:
    def __init__(self, z1: Tuple[float, float], z2: Tuple[float, float]) -> None:
        self.z1 = z1
        self.z2 = z2

    def add(self) -> Tuple[float, float]:
        return self.z1[0] + self.z2[0], self.z1[1] + self.z2[1]

    def multiply(self) -> Tuple[float, float]:
        erg = complex(self.z1[0], self.z1[1]) * complex(self.z2[0], self.z2[1])
        return erg.real, erg.imag

    def divide(self) -> Tuple[float, float]:
        erg = complex(self.z1[0], self.z1[1]) / complex(self.z2[0], self.z2[1])
        return erg.real, erg.imag


z1 = (5, 2)
z2 = (-1, -2)

sys = Complex(z1, z2)

print('Problem A')
print(sys.add())
print(sys.multiply())
print(sys.divide())
