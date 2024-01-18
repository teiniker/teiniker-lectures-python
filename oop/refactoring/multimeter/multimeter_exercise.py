import math

class Voltmeter():
    def __init__(self, name:str, range_min:float, range_max:float)->None:
        self.name = name
        self.unit = "[V]"
        self.range_min = range_min
        self.range_max = range_max

    def __str__(self)->str:
        return f"Voltmeter ({self.name}): range from {self.range_min} to {self.range_max} {self.unit}"

    def measured_value(self)->float:
        return 7.11 # simulate a measured value


class Amperemeter():
    def __init__(self, name:str, range_min:float, range_max:float)->None:
        self.name = name
        self.unit = "[A]"
        self.range_min = range_min
        self.range_max = range_max

    def __str__(self)->str:
        return f"Amperemeter ({self.name}): range from {self.range_min} to {self.range_max} {self.unit}"

    def measured_value(self)->float:
        return 0.02 # simulate a measured value


def is_in_range(instr, value:float)->bool:
    if value >= instr.range_min and value <= instr.range_max:
        return True
    else:
        return False


if __name__ == '__main__':

    fluke = Voltmeter("Fluke", 0.0, 10.0)
    print(fluke)
    assert "Voltmeter (Fluke): range from 0.0 to 10.0 [V]" == str(fluke)
    assert math.isclose(7.11, fluke.measured_value(), abs_tol=0.001)
    assert not is_in_range(fluke, 10.7)
    assert is_in_range(fluke, 1.7)

    keysight = Amperemeter("Keysight", 0.0, 0.1)
    print(keysight)
    assert "Amperemeter (Keysight): range from 0.0 to 0.1 [A]" == str(keysight)
    assert not is_in_range(keysight, -0.1)
    assert is_in_range(keysight, 0.1)
