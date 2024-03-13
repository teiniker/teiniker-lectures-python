
class Resistor():
    """Class using operator overloading and magic methods."""

    def __init__(self, value:int, tolerance:int=2) -> None:
        self.value = value
        self.tolerance = tolerance

    def __repr__(self) -> str:
        return f'Resistor({self.value}, {self.tolerance})'

    def __str__(self) -> str:
        return f'Resistor: value={self.value}, tolerance={self.tolerance}'

    def __eq__(self, other) -> bool:
        if self.value == other.value and self.tolerance == other.tolerance:
            return True
        else:
            return False

    def __add__(self, other): # if we use '+' Python invokes __add__()
        value = self.value + other.value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, tol_a, tol_b):
        if tol_a > tol_b:
            return tol_a
        return tol_b


if __name__ == '__main__':

    # Verify implementation
    r1 = Resistor(1000)
    assert 1000 == r1.value
    assert 2 == r1.tolerance

    r2 = Resistor(470,5)
    assert 470 == r2.value
    assert 5 == r2.tolerance

    r = Resistor(330, 2)
    assert 'Resistor(330, 2)' == repr(r)                # invoke __repr__()

    r = Resistor(330, 2)
    assert 'Resistor: value=330, tolerance=2' == str(r) # invoke __str__()

    r = r1 + r2                                         # invoke __add__()
    assert 1000+470 == r.value

    r1 = Resistor(2700,2)
    r2 = Resistor(2700,2)
    assert r1 is r1
    assert r1 == r2 # __eq__()
