
def fibonacci_numbers(size:int)->list[int]:
    """Calculate the Fibonacci sequence of a given size."""
    pass


if __name__ == '__main__':

    # Verify implementation
    assert [] == fibonacci_numbers(0)
    assert [0] == fibonacci_numbers(1)
    assert [0, 1] == fibonacci_numbers(2)
    assert [0, 1, 1] == fibonacci_numbers(3)
    assert [0, 1, 1, 2, 3, 5, 8] == fibonacci_numbers(7)
    assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377] == fibonacci_numbers(15)