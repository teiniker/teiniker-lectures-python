# Enumerations

Enumerations (Enums) are a **set of symbolic names (members) bound to
unique, constant values**. They are incredibly useful for defining a
collection of related, unchanging values, making code more readable,
maintainable, and less prone to errors compared to using raw strings
or integers.

We use Enums because of:

* **Readability**: Using names like `Weekday.MONDAY` is far more
    descriptive than `1` or `"Monday"`.

* **Preventing Invalid Values**: Enums restrict the possible values
    to a predefined set, preventing the use of invalid or misspelled
    inputs.

* **Maintainability**: If a value needs to change (e.g., a status
    code), it only needs to be updated in one place (the Enum
    definition).

## Defining an Enum

In Python, enumerations are created using the `Enum` class from the
built-in `enum` module. You define an Enum by subclassing `Enum` and
assigning attributes within the class body.

**Example: Defining a Weekday Enum**

Consider the `weekday.py` example found in this directory
(`oop/enumerations/weekday/weekday.py`). It defines a `Weekday`
enumeration:

```python
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
```

In this example, `MONDAY`, `TUESDAY`, etc., are the **members** of the
`Weekday` enum, and `1`, `2`, etc., are their corresponding **values**.

## Accessing Enum Members and Values

You can access enum members directly using dot notation, and their
`name` and `value` attributes:

```python
print(Weekday.TUESDAY)          # Output: Weekday.TUESDAY
print(Weekday.TUESDAY.name)     # Output: TUESDAY
print(Weekday.TUESDAY.value)    # Output: 2
```

You can also iterate over enum members:

```python
for day in Weekday:
    print(day)
# Output:
# Weekday.MONDAY
# Weekday.TUESDAY
# ...
```

Enums are particularly useful in situations where we need to map
symbolic names to other data or use them in conditional logic.

**Example: Mapping Enum Members**

The `weekday.py` example demonstrates mapping `Weekday` enum members
to German day names:

```python
day_map_german = {
    Weekday.MONDAY:'Montag',
    Weekday.TUESDAY:'Dienstag',
    Weekday.WEDNESDAY:'Mittwoch',
    Weekday.THURSDAY:'Donnerstag',
    Weekday.FRIDAY:'Freitag',
    Weekday.SATURDAY:'Samstag',
    Weekday.SUNDAY:'Sonntag'
}

def print_day_german(day):
    print(day_map_german[day])

print_day_german(Weekday.TUESDAY) # Output: Dienstag
```

**Example: Conditional Logic with Enums**

Enums significantly improve readability when used in conditional
statements:

```python
def is_working_day(day):
    if day == Weekday.MONDAY \
        or day == Weekday.TUESDAY \
        or day == Weekday.WEDNESDAY \
        or day == Weekday.THURSDAY \
        or day == Weekday.FRIDAY:
        return True
    else:
        return False

assert is_working_day(Weekday.WEDNESDAY) # True
assert not is_working_day(Weekday.SATURDAY) # True (because it's not a working day)
```

The full example can be found in `oop/enumerations/weekday/weekday.py`.
It showcases how to define an Enum and use its members in practical
functions, ensuring type safety and clear intent.

## Tutorials
* [YouTube: Using Enum in Python](https://youtu.be/gPPDXgCMZ0k)

## References
* [Python HOWTOs: Enum](https://docs.python.org/3.11/howto/enum.html)

*Egon Teiniker, 2020-2026, GPL v3.0*