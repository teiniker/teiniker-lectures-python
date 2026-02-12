from fibonacci import fibonacci_numbers

def test_fibonacci_numbers_zero():
    """Test case for fibonacci_numbers with size 0, expecting an empty list."""
    assert not fibonacci_numbers(0)

def test_fibonacci_numbers_one():
    """Test case for fibonacci_numbers with size 1, expecting [0]."""
    assert [0] == fibonacci_numbers(1)

def test_fibonacci_numbers_two():
    """Test case for fibonacci_numbers with size 2, expecting [0, 1]."""
    assert [0, 1] == fibonacci_numbers(2)

def test_fibonacci_numbers_three():
    """Test case for fibonacci_numbers with size 3, expecting [0, 1, 1]."""
    assert [0, 1, 1] == fibonacci_numbers(3)

def test_fibonacci_numbers_seven():
    """Test case for fibonacci_numbers with size 7, expecting the first 7 Fibonacci numbers."""
    assert [0, 1, 1, 2, 3, 5, 8] == fibonacci_numbers(7)

def test_fibonacci_numbers_fifteen():
    """Test case for fibonacci_numbers with size 15, expecting the first 15 Fibonacci numbers."""
    assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377] == fibonacci_numbers(15)
