# PyTest 

PyTest is currently the industry standard for Python testing, widely preferred over the built-in `unittest` 
module due to its simplicity, scalability, and powerful ecosystem.

When we run the `pytest` command, it performs the following steps:

* **Collection**: It searches your current directory and subdirectories for files starting with 
    `test_` or ending with `_test.py`.

* **Setup**: It initializes any necessary fixtures.

* **Execution**: It runs your test functions.

* **Teardown**: It cleans up fixtures.

* **Reporting**: It outputs a summary of passed, failed, and skipped tests.


## Setup 

```bash 
$ pip install pytest 

$ pytest --version
```


## Test Functions 

In pytest, **test functions are the basic building blocks** of our test suite. 
Each test function checks one small piece of behavior in our code.

A test function is simply a normal Python function that:
* starts with `test_`
* contains one or more `assert` statements

Test functions reside in files that also begin with `test_`.

Note that there are no separate `assert_equals()` operations. 
We simply use plain Python `assert` statements to verify behavior.

_Example:_ `test_fibonacci.py` 

```Python
from fibonacci import fibonacci_numbers

def test_fibonacci_numbers_zero():
    assert not fibonacci_numbers(0)

def test_fibonacci_numbers_one():
    assert [0] == fibonacci_numbers(1)

def test_fibonacci_numbers_two():
    assert [0, 1] == fibonacci_numbers(2)

def test_fibonacci_numbers_three():
    assert [0, 1, 1] == fibonacci_numbers(3)

def test_fibonacci_numbers_seven():
    assert [0, 1, 1, 2, 3, 5, 8] == fibonacci_numbers(7)
```

We run these tests from the command line:

```bash
$ pytest

========== test session starts ================================================
platform linux -- Python 3.13.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/student/github/teiniker-lectures-python/libraries/pytest/fibonacci
collected 6 items                                                                                                                         

test_fibonacci. py ......                                                [100%]
========== 6 passed in 0.02s ==================================================
```

Note that `pytest` will run all files of the form `test_*.py` or `*_test.py` 
in the current directory and its subdirectories.

Common flags you can use when running `pytest` include:

* `-s`, `--capture=no`: Output print statements. 

* `-v`, `--verbose`: Increase verbosity

Possible outcomes of a test: 

* **PASSED (.)**: The test ran successfully. 

* **FAILED (F)**: The test did not run successfully. 

* **SKIPPED (s)**: The test was skipped. We can tell pytest to skip a test by using either 
    the `@pytest.mark.skip()` or `@pytest.mark.skipif()` decorators.

* **ERROR (E)**: An exception happened either during the execution of a fixture or 
    hook function, and not during the execution of a test function.


### Using assert Statements 

When we write test functions, the normal Python `assert` statement is our 
primary tool to communicate test failure.

pytest includes a feature called **assert rewriting** that intercepts `assert` 
calls and replaces them with something that can tell us more about why our 
assertions failed.

_Examples:_ pytest assert statements

* `assert something` 

* `assert not something` 

* `assert a == b`

* `assert a != b` 

* `assert a is None` 

* `assert a is not None` 

With pytest, we can use `assert <expression>` with any expression.

We can also use `pytest.fail()` as a manual way to **immediately fail** a test 
with a clear message, even if no assertion has failed yet.


### Compare Floating-Point Values

We can use `pytest.approx()` to compare floating-point values that may have 
small rounding errors.

_Example:_ Compare floating-point values

```Python
def test_sum():
    assert (0.1 + 0.2) == pytest.approx(0.3)
```

`pytest.approx()` checks whether numbers are close enough within a tolerance, 
not exactly equal.

- `pytest.approx(expected)`: The default values are `rel = 1e-6`and `abs = 1e-12`, 
    `pytest` chooses whichever allows the larger window.

- `pytest.approx(expected, abs=...)`: When numbers near zero

- `pytest.approx(expected, rel=...)`: When values scale larger


This avoids the need for manual tolerance checks or using `math.isclose` 
and works with scalars, lists, and NumPy arrays.


### Testing Exceptions

In pytest, testing exceptions is clean and explicit.
We verify that a specific error is raised at the right moment using
`pytest.raises(...)`.

_Example:_ Basic exception test

```Python
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

In this example, the code inside the with block must raise `ZeroDivisionError`:
* if it doesn’t: test fails
* if a different exception is raised: test fails
* if `ZeroDivisionError` is raised: test succeeds

_Example:_ Multiple possible exceptions

```Python
with pytest.raises((ValueError, TypeError)):
    some_function()
```


_Example: Testing the exception message

```Python
def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(10, 0)
```

* `match=` checks the error text using **regex**.


_Example:_ Capturing the exception object

```Python
def test_exception_details():
    with pytest.raises(ValueError) as exc:
        int("abc")
    assert "invalid literal" in str(exc.value)
```
* `exc.value` is the actual exception instance.


## Test Classes 

In pytest, we can **organize related tests** inside test classes.

They’re lightweight (much simpler than `unittest.TestCase`) and 
exist mainly for grouping + shared fixtures.

A pytest test class is:
* a normal Python class
* named starting with `Test`
* containing methods starting with `test_`

_Example:_ Test class

```Python 
class TestResistor:
    def test_initial_value(self):
        r1 = Resistor(100, 1)
        assert self.r1.value == 100
        assert self.r1.tolerance == 1

    def test_value_setter(self):
        r1 = Resistor(100, 1)
        self.r1.value = 470
        assert self.r1.value == 470

    def test_add_resistors(self):
        r1 = Resistor(100, 1)
        r2 = Resistor(330, 5)
        r_sum = self.r1 + r2
        assert r_sum.value == 100 + 330
        assert r_sum.tolerance == 5
```


### Object-Level Setup/Teardown

`setup_method()` and `teardown_method()` are special lifecycle 
hooks that **run before and after each test method** in a test class.
They are inspired by xUnit-style testing (like unittest).

_Example:_ 

```Python 
class TestResistor:
    def setup_method(self, method):
        self.r1 = Resistor(100, 1)

    def teardown_method(self, method):
        print("teardown_method called")
```

Using `def setup_method(self, method)`:
* `method` is the actual test function object being executed.

Note that pytest creates a **new instance of the class for every test method**.
Thus, state does NOT leak between tests.


### Class-Level Setup/Teardown

`setup_class()` and `teardown_class()` are class-level lifecycle hooks.
They **run once per test class**, not before every test like `setup_method()`.
They’re part of pytest’s built-in xUnit-style support.

```Python 
class TestDatabase:

    @classmethod
    def setup_class(cls):
        self.db = connect_to_test_db()

    @classmethod
    def teardown_class(cls):
        self.db.close()
```

* `cls` is the class object itself, allowing you to store and share 
    data across all instances.
    It’s the class-level equivalent of `self`.


## Fixtures

In pytest, fixtures are the modern, powerful **replacement for `setup_*` 
and `teardown_*` methods**.

A fixture is a function marked with: `@pytest.fixture` that:
* prepares something a test needs
* provides it to the test
* optionally cleans it up afterward

A fixture is only available for tests to request if they are in the 
scope that fixture is defined in:

* If a fixture is defined inside a class, it can only be requested 
    by tests inside that class. 

* If a fixture is defined inside the global scope of the module, 
    then every test in that module, even if it’s defined inside a 
    class, can request it.

_Example:_ Fixture setup

```Python
class TestResistor:

    @pytest.fixture
    def resistor(self):
        # Setup 
        return Resistor(100, 1)

    def test_initial_value(self, resistor):
        assert resistor.value == 100
        assert resistor.tolerance == 1
```

In this example, we define a fixture inside a test class and inject it 
automatically into test methods.

The `resistor()` fixture tells pytest that if a test requests `resistor`, 
it should create and provide a `Resistor(100, 1)` instance.

Because `resistor`is a function argument, pytest:
* Looks for a fixture called resistor
* Calls the fixture function
* Passes the result into the test


_Example:_ Fixture setup and teardown

This is a pytest fixture with teardown using the **yield pattern**. 
It’s the pytest `setup → provide → cleanup` idiom.

```Python
@pytest.fixture
def resistor():
    # Setup (runs before the test)
    r = Resistor(100, 1)
    
    # Hands the object to the test
    yield r
    
    # Teardown (runs after the test, even on failure)
    r.cleanup()
```

* **Setup**: Create the object in a known state (value 100, tolerance 1).

* `yield` returns `r` to the test but does not end the fixture. 
    Instead, pytest pauses the fixture right there.
    So the test receives r as the value of the resistor argument.

* **Teardown**: After the test finishes (pass, fail, or error), pytest 
    resumes the fixture function after the `yield` and executes 
    the cleanup code.


## Running a Subset of Tests

Running just a small batch of tests is handy while debugging or if we 
want to limit the tests to a specific section of the code base we are 
working on at the time.

pytest allows you to run a subset of tests in several ways: 

* **Single test function**: `pytest path/test_module.py::test_function`

* **All tests in a module**: `pytest path/test_module.py`

* **Single test method**: `pytest path/test_module.py::TestClass::test_method` 

* **All tests in a class**: `pytest path/test_module.py::TestClass`

* **All tests in a directory**: `pytest path Tests matching a name pattern pytest -k pattern`



## References

* [YouTube: Pytest Tutorial - How to Test Python Code](https://youtu.be/cHYq1MRoyI0?si=HkkHzKJwXz1GQiyO)

* [pytest](https://docs.pytest.org/en/stable/)

2022)

* Brian Okken. **Python Testing with pytest: Simple, Rapid, Effective, and Scalable**. The Pragmatic Programmers, 2nd edition 2022. 

*Egon Teiniker, 2020-2026, GPL v3.0*