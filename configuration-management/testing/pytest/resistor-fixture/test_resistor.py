import pytest
from resistor import Resistor

class TestResistor:
    """Tests for the Resistor class."""

    @pytest.fixture
    def resistor(self):
        """Fixture to create a default Resistor object for testing."""
        print("resistor fixture called")
        return Resistor(100, 1)

    def test_initial_value(self, resistor):
        """Test that the Resistor object is initialized with the correct value and tolerance."""
        assert resistor.value == 100
        assert resistor.tolerance == 1

    def test_value_setter(self, resistor):
        """Test that the value setter correctly updates the resistor's value."""
        resistor.value = 470
        assert resistor.value == 470

    def test_add_resistors(self, resistor):
        """Test the addition of two Resistor objects."""
        r2 = Resistor(330, 5)
        r_sum = resistor + r2
        assert r_sum.value == 100 + 330
        assert r_sum.tolerance == 5
