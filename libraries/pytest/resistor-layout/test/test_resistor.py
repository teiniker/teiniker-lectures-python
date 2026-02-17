from parts.resistor import Resistor

class TestResistor:
    """Tests for the Resistor class."""

    def setup_method(self):
        """Set up a default Resistor object for testing."""
        print("setup_method called")
        self.r1 = Resistor(100, 1)

    def teardown_method(self):
        """Clean up after each test method."""
        print("teardown_method called")

    def test_initial_value(self):
        """Test that the Resistor object is initialized with the correct value and tolerance."""
        assert self.r1.value == 100
        assert self.r1.tolerance == 1

    def test_value_setter(self):
        """Test that the value setter correctly updates the resistor's value."""
        self.r1.value = 470
        assert self.r1.value == 470

    def test_add_resistors(self):
        """Test the addition of two Resistor objects."""
        r2 = Resistor(330, 5)
        r_sum = self.r1 + r2
        assert r_sum.value == 100 + 330
        assert r_sum.tolerance == 5
