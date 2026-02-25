# Packages

A package is essentially a directory that organizes modules (Python files) 
in a hierarchical structure. Packages help in structuring the code and make 
it easier to manage large codebases by grouping related modules together.

* **Directory with `__init__.py`**: A package is identified by the presence 
    of an `__init__.py` file in a directory. This file can be empty or execute 
    initialization code for the package.

* **Hierarchical Structure**: Packages can contain sub-packages, which in 
    turn can contain their own modules and sub-packages. This creates a 
    nested, tree-like structure.

* **Namespace Organization**: By using packages, we avoid naming conflicts 
    between modules with the same name that reside in different packages.

* **Importing**: We can import modules from a package using **dot notation**. 
    For example, if we have a package named `mypackage` with a module 
    `mymodule`, we can import it with `from mypackage import mymodule`.


_Example_: Package structure (filesystem).
```Bash
├── main.py
└── org
    ├── __init__.py
    └── se
        ├── __init__.py
        └── lab
            ├── date.py
            └── __init__.py
```
* Python recognizes `org`, `se`, and `lab` as packages because each 
    directory contains an `__init__.py` file.

_Example_: Access a module's function from a package (`main.py`).
```Python
from org.se.lab.date import is_leap_year

if __name__ == '__main__':
    # Verify implementation
    assert is_leap_year(2000)
    assert is_leap_year(2020)
    assert not is_leap_year(2021)
    assert not is_leap_year(2100)
```

* The import statement uses the full package path starting from 
    the top-level directory where `main.py` resides.

*  Importing using from `org.se.lab.date` import `is_leap_year` 
    directly accesses the functions defined in `date.py`.

Alternatively, you can import the module using the following syntax:

```Python
import org.se.lab.date as date

if __name__ == '__main__':
    # Verify implementation
    assert date.is_leap_year(2000)
    assert date.is_leap_year(2020)
    assert not date.is_leap_year(2021)
    assert not date.is_leap_year(2100)
```

## References

* [Python Tutorial: Packages](https://docs.python.org/3/tutorial/modules.html#packages)

*Egon Teiniker, 2020-2025, GPL v3.0*
