class Resistor():
    def __init__(self, value:int, tolerance:int=2)->None:
        self.tolerance = tolerance
        self.value= value

    def __str__(self)->str:
        return f'Resistor: value={self.value}Ohm, tolerance={self.tolerance}%'


class Capacitor():
    def __init__(self, value:int, tolerance:int=5)->None:
        self.tolerance = tolerance
        self.value= value

    def __str__(self)->str:
        return f'Capacitor: value={self.value}uF, tolerance={self.tolerance}%'


# Duck typing (whatever part is - use str() to print it)
def print_part(part)->None:
    print(f"Part: {part}")


if __name__ == '__main__':

    # Verify implementations
    r1 = Resistor(1000)
    assert 1000 == r1.value
    assert 2 == r1.tolerance

    r2 = Resistor(470,5)
    assert 470 == r2.value
    assert 5 == r2.tolerance

    r = Resistor(330, 2)
    assert 'Resistor: value=330Ohm, tolerance=2%' == str(r)

    c1 = Capacitor(1)
    assert 1 == c1.value
    assert 5 == c1.tolerance

    c2 = Capacitor(100, 10)
    assert 100 == c2.value
    assert 10 == c2.tolerance

    assert 'Capacitor: value=1uF, tolerance=5%' == str(c1)

    print_part(r1)  # r1 "is a " Part
    print_part(c1)  # c1 "is a " Part
