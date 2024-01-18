class Resistor():
    """Model of a resistor with a given tolerance."""

    def __init__(self, value:int, tolerance:int)->None:
        self.value = value
        self.tolerance = tolerance

    @property
    def value(self)->int:
        return self._value

    @value.setter
    def value(self, value:int):
        if value < 0:
            raise ValueError('Invalid value!')
        self._value = value

    @property
    def tolerance(self)->int:
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance:int):
        if tolerance < 0:
            raise ValueError('Invalid tolerance!')
        self._tolerance = tolerance


    def __add__(self, other:"Resistor"):
        value = self._value + other._value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, value_a, value_b):
        if value_a > value_b:
            return value_a
        else:
            return value_b


if __name__ == '__main__':

    # Verify implementation

#    r1 = Resistor(-1000, 1)

    # try:
    #     r1 = Resistor(1000, -1)
    #     #...
    # except ValueError as e:
    #     print(f"Resistor object can't be created: {e}")


    # try:
    #     r1 = Resistor(-1000, 2)
    #     #...

    # except ValueError as e:
    #     print(f"Resistor object can't be created: {e}")
    # finally:
    #     print("Do some clean-up.")


    try:
        r1 = Resistor(-1000, 1)
        #...
    except ValueError as e:
        print(f"Resistor object can't be created: {e}")
    else:
        print("No exception thrown.")
