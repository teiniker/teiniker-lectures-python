# Inheritance

In object-oriented programming, **inheritance** is a powerful mechanism that
allows a new class (called a **subclass** or **child class**) to be based
on an existing class (the **superclass** or **parent class**). The child
class "inherits" the attributes and methods of the parent class, allowing
for code reuse and the creation of a logical "is-a" relationship.

For example, a `Car` is a `Vehicle`. The `Car` class can inherit common
properties from the `Vehicle` class (like `speed` and `color`) while
adding its own specific properties (like `trunk_size`).


## Code Duplication and Duck Typing

Let's start with a situation where we have two classes, `Resistor` and
`Capacitor`, that are conceptually similar but have no formal relationship.

**Example: `resistor_capacitor1.py`**

```python
class Resistor():
    def __init__(self, value, tolerance=2):
        self.tolerance = tolerance
        self.value= value
    def __str__(self):
        return f'Resistor: value={self.value}Ohm, tolerance={self.tolerance}%'

class Capacitor():
    def __init__(self, value, tolerance=5):
        self.tolerance = tolerance
        self.value= value
    def __str__(self):
        return f'Capacitor: value={self.value}uF, tolerance={self.tolerance}%'

# Duck typing (whatever part is - use str() to print it)
def print_part(part):
    print(f"Part: {part}")

print_part(Resistor(1000))  # Works
print_part(Capacitor(10))   # Works
```

This works because of **duck typing** ("if it walks like a duck and quacks
like a duck, it must be a duck"). The `print_part()` function doesn't care
about the object's actual type, only that it can be converted to a string.
However, this approach has drawbacks: there's significant code duplication,
and we aren't formally stating that `Resistor` and `Capacitor` are both
types of electronic parts.


## Solution: A Common Base Class

Inheritance solves this by creating a common parent class that holds all
the shared logic.

**Example: `resistor_capacitor2.py`**

We can create a `Part` class to contain the shared `value` and `tolerance`
attributes. `Resistor` and `Capacitor` can then inherit from `Part`.

```python
class Part():   # Base Class (aka Super Class)
    def __init__(self, value, tolerance):
        self.tolerance = tolerance
        self.value= value

class Resistor(Part):   # Sub-Class
    def __init__(self, value, tolerance=2):
        super().__init__(value, tolerance) # Call parent's __init__

    def __str__(self): # Override parent's default behavior
        return f'Resistor: value={self.value}Ohm, tolerance={self.tolerance}%'

class Capacitor(Part):  # Sub-Class
    def __init__(self, value, tolerance=5):
        super().__init__(value, tolerance)

    def __str__(self): # Override parent's default behavior
        return f'Capacitor: value={self.value}uF, tolerance={self.tolerance}%'
```

Key concepts here are:

* **Inheritance**: `Resistor(Part)` declares that `Resistor` is a subclass of `Part`.

* **`super()`**: The `super().__init__(...)` line in the child's `__init__`
    method calls the parent's `__init__` method, ensuring that the parent's
    logic is executed.

* **Method Overriding**: Both `Resistor` and `Capacitor` provide their own
    specific implementation of the `__str__` method. This is called overriding.

* **Polymorphism**: A function like `print_part(part: Part)` can now accept
    any object that "is-a" `Part` (i.e., an instance of `Part` or any of its
    subclasses). This is a core benefit of inheritance.


## Enforcing a Contract: Abstract Base Classes (ABCs)

Sometimes, we want to create a base class that defines a "contract" for
its children but should never be instantiated itself. This is an **abstract
base class**. An ABC can declare **abstract methods**, which all child
classes *must* implement.

**Example: `resistor_capacitor3.py`**

In this example, `Part` is an abstract base class. It defines the common
interface for all parts, but you cannot create a generic `Part` instance.
The `abc` module is used to achieve this.

```python
from abc import ABC

class Part(ABC): # Inherit from ABC
    def __init__(self, value, tolerance):
        self.tolerance = tolerance
        self.value= value

class Resistor(Part):
    def __init__(self, value, tolerance=2):
        super().__init__(value, tolerance)

    def __str__(self):
        return f'Resistor: value={self.value}Ohm, tolerance={self.tolerance}%'

class Capacitor(Part):
    def __init__(self, value, tolerance=5):
        super().__init__(value, tolerance)

    def __str__(self):
        return f'Capacitor: value={self.value}uF, tolerance={self.tolerance}%'
```

If a subclass were to be created without the required methods (if any
were declared abstract with `@abstractmethod`), Python would raise a
`TypeError` when you try to create an instance of it. This is a powerful
way to enforce a consistent API across a family of classes.


## Improving Clarity with Type Hints

Modern Python encourages the use of type hints to improve code readability
and allow for static analysis (checking for type errors before running the
code).

**Example: `resistor_capacitor4.py`**

This example refactors our `Part` hierarchy to include type hints.

```python
class Part(ABC):
    def __init__(self, value:int, tolerance:int):
        self.tolerance = tolerance
        self.value= value

class Resistor(Part):
    def __init__(self, value:int, tolerance:int=2):
        super().__init__(value, tolerance)

def print_part(part:Part) -> None:
    print(f"Part: {part}")
```

While this doesn't change how the code runs, it makes the intent clear: the
`value` should be an `int`, and `print_part` expects an object that conforms
to the `Part` interface.


## Tutorials
* [YouTube (Corey Schafer): Inheritance - Creating Subclasses](https://youtu.be/RSl87lqOXDE)


## References

*Egon Teiniker, 2020-2026, GPL v3.0*
