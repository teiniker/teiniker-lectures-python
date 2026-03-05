import pytest

@pytest.fixture
def simpsons():
    return ["homer", "marge", "bart"]

def test_list_equal(simpsons):
    expected = ["homer", "marge", "bart"]
    assert simpsons == expected

def test_count_equal(simpsons):
    expected = ["homer", "marge", "bart"]
    assert sorted(simpsons) == sorted(expected)

def test_list_index(simpsons):
    assert simpsons[1] == "marge"
    assert simpsons[-1] == "bart"

def test_list_size(simpsons):
    assert len(simpsons) == 3

def test_list_modify_element(simpsons):
    simpsons[2] = "lisa"
    expected = ["homer", "marge", "lisa"]
    assert simpsons == expected

def test_list_append(simpsons):
    simpsons.append("lisa")
    expected = ["homer", "marge", "bart", "lisa"]
    assert simpsons == expected

def test_list_insert(simpsons):
    simpsons.insert(1, "lisa")
    expected = ["homer", "lisa", "marge", "bart"]
    assert simpsons == expected

def test_list_delete_element(simpsons):
    del simpsons[1]
    expected = ["homer", "bart"]
    assert simpsons == expected

def test_list_pop(simpsons):
    string = simpsons.pop()
    expected = ["homer", "marge"]
    assert simpsons == expected
    assert string == "bart"

def test_list_pop_with_index(simpsons):
    string = simpsons.pop(1)
    expected = ["homer", "bart"]
    assert simpsons == expected
    assert string == "marge"

def test_list_remove(simpsons):
    simpsons.remove("homer")
    expected = ["marge", "bart"]
    assert simpsons == expected

def test_list_sort(simpsons):
    simpsons.sort()
    expected = ["bart", "homer", "marge"]
    assert simpsons == expected

def test_list_reverse(simpsons):
    simpsons.reverse()
    expected = ["bart", "marge", "homer"]
    assert simpsons == expected

def test_list_slice(simpsons):
    sublist = simpsons[1:2]  # [from:to)
    expected = ["marge"]
    assert sublist == expected

def test_list_range():
    num_list = list(range(3, 7))  # [from:to)
    expected = [3, 4, 5, 6]
    assert num_list == expected
