# Example: Testing List with pytest

A **list** is a **collection of items in a particular order**.
Square brackets `[]` indicate a list, and individual elements 
in the list are separated by commas.

## Setup Phase

With **pytest**, shared test setup is typically done with a fixture.
The fixture is created for each test that uses it.

```python
import pytest

@pytest.fixture
def simpsons():
    return ["homer", "marge", "bart"]
```

## Test Cases

To **access an element in a list**, use the list name followed by the 
index in square brackets.
Index `-1` always returns the last item in the list.

```python
def test_list_index(simpsons):
    assert simpsons[1] == "marge"
    assert simpsons[-1] == "bart"
```

The function `len()` returns the **length of a list**.

```python
def test_list_size(simpsons):
    assert len(simpsons) == 3
```

To **change an element**, assign a new value at the given index.

```python
def test_list_modify_element(simpsons):
    simpsons[2] = "lisa"
    expected = ["homer", "marge", "lisa"]
    assert simpsons == expected
```

The simplest way to **add a new element** to a list is `append()`.

```python
def test_list_append(simpsons):
    simpsons.append("lisa")
    expected = ["homer", "marge", "bart", "lisa"]
    assert simpsons == expected
```

We can **add a new element at any position** with `insert(index, value)`.

```python
def test_list_insert(simpsons):
    simpsons.insert(1, "lisa")
    expected = ["homer", "lisa", "marge", "bart"]
    assert simpsons == expected
```

If we know the **position of the item we want to remove**, use `del`.

```python
def test_list_delete_element(simpsons):
    del simpsons[1]
    expected = ["homer", "bart"]
    assert simpsons == expected
```

The `pop()` method **removes the last item** and returns it.

```python
def test_list_pop(simpsons):
    s = simpsons.pop()
    expected = ["homer", "marge"]
    assert simpsons == expected
    assert s == "bart"
```

We can use `pop(index)` to **remove an item at any position**.

```python
def test_list_pop_with_index(simpsons):
    s = simpsons.pop(1)
    expected = ["homer", "bart"]
    assert simpsons == expected
    assert s == "marge"
```

If we only know the value of the item, use `remove(value)`.

```python
def test_list_remove(simpsons):
    simpsons.remove("homer")
    expected = ["marge", "bart"]
    assert simpsons == expected
```

The `sort()` method **changes the order permanently**.

```python
def test_list_sort(simpsons):
    simpsons.sort()
    expected = ["bart", "homer", "marge"]
    assert simpsons == expected
```

To **reverse the original order**, use `reverse()`.

```python
def test_list_reverse(simpsons):
    simpsons.reverse()
    expected = ["bart", "marge", "homer"]
    assert simpsons == expected
```

To **make a slice**, specify start and end index `[from:to)`.

```python
def test_list_slice(simpsons):
    sublist = simpsons[1:2]
    expected = ["marge"]
    assert sublist == expected
```

When we wrap `list()` around a call to `range()`, the output is a **list of numbers**.

```python
def test_list_range():
    num_list = list(range(3, 7))
    expected = [3, 4, 5, 6]
    assert num_list == expected
```

## Assertions in pytest

pytest encourages plain Python `assert` statements.

```python
def test_list_equal(simpsons):
    expected = ["homer", "marge", "bart"]
    assert simpsons == expected
```

For comparisons where order should not matter, compare sorted lists.

```python
def test_count_equal(simpsons):
    expected = ["homer", "marge", "bart"]
    assert sorted(simpsons) == sorted(expected)
```

*Egon Teiniker, 2020-2026, GPL v3.0*
