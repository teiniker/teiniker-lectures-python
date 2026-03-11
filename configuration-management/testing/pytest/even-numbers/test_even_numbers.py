import pytest
from even_numbers import even_numbers

def test_even_numbers():
    # Setup
    numbers = [5, 2, 1, 8, 4]
    # Exercise
    result = even_numbers(numbers)
    # Verify
    assert [2, 8, 4] == result
    # Teardown (not needed in this case)

def test_empty_list():
    numbers = []
    result = even_numbers(numbers)
    assert not result # []

def test_all_odd_numbers():
    numbers = [1, 3, 5, 7]
    result = even_numbers(numbers)
    assert not result # []

def test_none_input():
    with pytest.raises(ValueError):
        even_numbers(None)
