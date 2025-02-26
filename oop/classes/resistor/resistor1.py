
class Resistor():
    """Class implementation at its simplest."""
    def __init__(self, value, tolerance):
        self.value = value
        self.tolerance = tolerance

    def add(self, other):
        value = self.value + other.value
        if self.tolerance > other.tolerance:
            tolerance = self.tolerance
        else:
            tolerance = other.tolerance
        return Resistor(value, tolerance)


if __name__ == '__main__':

    # Verify implementation
    r1 = Resistor(100,1)    # invoke __init__() => Resistor instance
    assert 100 == r1.value
    assert 1 == r1.tolerance

    r2 = Resistor(330,5)
    assert 330 == r2.value
    assert 5 == r2.tolerance

    r = r1.add(r2)
    assert 100+330 == r.value
    assert 5 == r.tolerance

    r3 = Resistor(1000, 1)
    r4 = r.add(r3)
    print(r4.value)
    assert 100+330+1000 == r4.value
