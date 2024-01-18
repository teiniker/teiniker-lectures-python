
class Resistor():
    def __init__(self, value:int, tolerance:int):
        self.value = value
        self.tolerance = tolerance

    @property
    def value(self) -> int:
        print(f'get value: {self._value}')
        return self._value

    @value.setter
    def value(self, value:int):
        print(f'set value: {value}')
        self._value = value

    @property
    def tolerance(self) -> int:
        print(f'get tolerance: {self._tolerance}')
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance:int):
        print(f'set tolerance: {tolerance}')
        self._tolerance = tolerance

    def __add__(self, other):   # + operator
        value = self._value + other._value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, tol_a, tol_b):
        if tol_a > tol_b:
            return tol_a
        return tol_b


if __name__ == '__main__':

    # Verify implementation
    r1 = Resistor(100,1)
    assert 100 == r1.value          # invoke value()
    assert 1 == r1.tolerance        # invoke tolerance()

    r2 = Resistor(330,5)
    r2.value = 470                  # invoke value(470)
    assert 470 == r2.value
    assert 5 == r2.tolerance

    r = r1 + r2                     # invoke __add__()
    assert 100+470 == r.value
    assert 5 == r.tolerance
