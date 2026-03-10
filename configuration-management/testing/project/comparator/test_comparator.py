from comparator import compare

def test_a_gt_b():
    assert compare(7, 3) == 1

def test_a_lt_b():
    assert compare(3, 7) == -1

def test_a_eq_b():
    assert compare(7, 7) == 0

