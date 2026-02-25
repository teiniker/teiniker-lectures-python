# Data Classes

In Python, we can use the `dataclass` decorator to implement a data class.

A data class is **a class that is primarily used to store data** and has minimal or no methods. It provides a concise way to define a class with default behaviors for `init`, 
`repr`, `eq`, and more.

_Example:_ 

The dataclass decorator automatically generates default implementations of `__init__()`, `__repr__()`, and `__eq__()` methods based on the attributes of the class. 

```Python 
@dataclass
class Article:
    oid:int
    description:str
    price:int
```

Note that we can also override the `__eq__()` method in our `Article` class to compare only the `oid` attribute.


## References

* [The Python Standard Library: dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html)

* [PEP 557 – Data Classes](https://peps.python.org/pep-0557/)

*Egon Teiniker, 2020-2026, GPL v3.0*