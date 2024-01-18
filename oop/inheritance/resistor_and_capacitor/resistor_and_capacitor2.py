class Part():   # Base Class (aka Super Class)
    def __init__(self, value:int, tolerance:int)->None:
        self.tolerance = tolerance
        self.value= value


class Resistor(Part):   # Sub-Class
    def __init__(self, value:int, tolerance:int=2)->None:
        super().__init__(value, tolerance)

    def __str__(self)->str:
        return f'Resistor: value={self.value}Ohm, tolerance={self.tolerance}%'


class Capacitor(Part):  # Sub-Class
    def __init__(self, value:int, tolerance:int=5)->None:
        super().__init__(value, tolerance)

    def __str__(self)->str:
        return f'Capacitor: value={self.value}uF, tolerance={self.tolerance}%'


# Use base type as parameter (polymorphism)

def print_part(part:Part)->None:
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

    assert isinstance(r1, Resistor)
    assert isinstance(r1, Part)
    assert not isinstance(r1, Capacitor)

    assert issubclass(Resistor, Part)
    assert issubclass(Capacitor, Part)
    assert not issubclass(Resistor, Capacitor)

    print_part(r1)  # r1 "is a " Part
    print_part(c1)  # c1 "is a " Part
