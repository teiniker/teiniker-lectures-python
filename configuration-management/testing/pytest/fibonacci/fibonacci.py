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
