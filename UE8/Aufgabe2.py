class Poly:
    def __init__(self, coeffs: list):
        self.coeffs = coeffs

    # @classmethod Can't access self then ??
    def poly_eval(self, x: float):
        return sum([self.coeffs[i] * x**i for i in range(len(self.coeffs))])

    def poly_der_coef(self, k: int) -> list:
        coeffs = self.coeffs.copy()
        for _ in range(k):
            coeffs = self.__derive(coeffs)
        return coeffs

    @staticmethod
    def __derive(coeffs: list) -> list:
        if len(coeffs) == 0:
            return []
        for i in range(len(coeffs) - 1):
            coeffs[i] = (i+1) * coeffs[i+1]
        coeffs.pop(-1)      # remove last element
        return coeffs


test_polynomial = [1, -2, 0, 0, 1, -10]

polynom_function = Poly(test_polynomial)
print('x: 5, Output:', polynom_function.poly_eval(5))       # should be -30 634

derived_polynom_function = Poly(polynom_function.poly_der_coef(1))
print('Derived once, x: 5, Output:', derived_polynom_function.poly_eval(5))     # should be -30 752

derived_5_times = Poly(polynom_function.poly_der_coef(5))
print('Derived 5 times:', derived_5_times.poly_eval(5))     # should be -1 200
