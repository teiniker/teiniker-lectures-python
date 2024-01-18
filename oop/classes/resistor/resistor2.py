
class Resistor():
    """Class using private attributes together with getter and setter methods."""
    def __init__(self, value:int, tolerance:int) -> None:
        self.__value = value
        self.__tolerance = tolerance

    def get_value(self):
        return self.__value

    def set_value(self, value:int) -> None:
        self.__value = value

    def get_tolerance(self) -> int:
        return self.__tolerance

    def set_tolerance(self, tolerance:int) -> None:
        self.__tolerance = tolerance

    def add(self, other):
        value = self.__value + other.get_value()
        tolerance = self.__max(self.__tolerance, other.get_tolerance())
        return Resistor(value, tolerance)

    def __max(self, tol_a, tol_b):
        if tol_a > tol_b:
            return tol_a
        return tol_b

if __name__ == '__main__':

    # Verify implementation
    r1 = Resistor(100,1)
    assert 100 == r1.get_value()
    assert 1 == r1.get_tolerance()

    r2 = Resistor(330,5)
    assert 330 == r2.get_value()
    assert 5 == r2.get_tolerance()

    r = r1.add(r2)
    assert 100+330 == r.get_value()
    assert 5 == r.get_tolerance()
