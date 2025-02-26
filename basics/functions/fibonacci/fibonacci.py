def fibonacci_numbers(size):
    """Calculate the Fibonacci sequence of a given size."""
    if size <= 0:
        return []
    elif size == 1:
        return [0]
    else:
        sequence = [0,1]
        count = 2
        while count < size:
            sequence.append(sequence[count-2] + sequence[count-1])
            count += 1
        return sequence


if __name__ == '__main__':

    # Verify implementation
    assert not fibonacci_numbers(0)
    assert [0] == fibonacci_numbers(1)
    assert [0, 1] == fibonacci_numbers(2)
    assert [0, 1, 1] == fibonacci_numbers(3)
    assert [0, 1, 1, 2, 3, 5, 8] == fibonacci_numbers(7)
    assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377] == fibonacci_numbers(15)
