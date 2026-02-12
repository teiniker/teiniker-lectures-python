
class Resistor():
    """Represents an electrical resistor with a given value and tolerance."""
    def __init__(self, value, tolerance):
        """
        Initializes a Resistor object.

        Args:
            value (int/float): The resistance value in ohms.
            tolerance (int/float): The tolerance percentage.
        """
        self.value = value      # invoke value(value)
        self.tolerance = tolerance

    @property
    def value(self):
        """Get the resistance value."""
        print(f'get value: {self._value}')
        return self._value

    @value.setter
    def value(self, value):
        """Set the resistance value."""
        print(f'set value: {value}')
        self._value = value

    @property
    def tolerance(self):
        """Get the tolerance percentage."""
        print(f'get tolerance: {self._tolerance}')
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Set the tolerance percentage."""
        print(f'set tolerance: {tolerance}')
        self._tolerance = tolerance

    def __add__(self, other):   # + operator
        """
        Adds two Resistor objects together (simulating series connection).

        Args:
            other (Resistor): The other Resistor object to add.

        Returns:
            Resistor: A new Resistor object representing the sum.
        """
        value = self._value + other._value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, tol_a, tol_b):
        """
        Returns the maximum of two tolerance values.

        Args:
            tol_a (int/float): First tolerance value.
            tol_b (int/float): Second tolerance value.

        Returns:
            int/float: The greater of the two tolerance values.
        """
        if tol_a > tol_b:
            return tol_a
        return tol_b

