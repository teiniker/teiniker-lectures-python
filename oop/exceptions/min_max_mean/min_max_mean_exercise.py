def min_value(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

def max_value(lst):
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

def mean_value(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':

    try:
        min_value([])
        assert False
    except ValueError:
        pass  # Exception was raised as expected

    try:
        max_value([])
        assert False
    except ValueError:
        pass  # Exception was raised as expected

    try:
        mean_value([])
        assert False
    except ValueError:
        pass  # Exception was raised as expected
