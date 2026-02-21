from electronics import parts

def test_class_variable():
    # Setup
    # Exercise
    vendor = parts.Resistor.vendor
    # Verify
    assert 'Neuhold Electronics' == vendor
    # Teardown

def test_resistor_init():
    # Setup
    res = parts.Resistor(470, 5)
    # Exercise
    value = res.value
    tol = res.tolerance
    # Verify
    assert 470 == value
    assert 5 == tol
    # Teardown

def test_default_value():
    # Setup
    res = parts.Resistor(1000)
    assert 1000 == res.value
    assert 2 == res.tolerance


def test_add_resistors():
    # Setup
    res_1 = parts.Resistor(1000)
    res_2 = parts.Resistor(330)
    # Exercise
    res = res_1 + res_2
    # Verify
    assert 1000+330 == res.value
    assert 2 == res.tolerance
    # Teardown
