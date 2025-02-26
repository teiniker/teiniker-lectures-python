# Multiple return values of a function

def swap_value(value_a, value_b):
    """Change the values of a and b"""
    return value_b, value_a


if __name__ == '__main__':
    A = 7
    B = 11
    A,B = swap_value(A,B)
    assert A == 11
    assert B == 7
