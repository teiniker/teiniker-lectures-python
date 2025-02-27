# Modules

As our program gets longer, we may want to split it into several files 
for easier maintenance.

To support this, **Python has a way to put definitions in a file and use 
them in a script or in an interactive instance of the interpreter**. 
Such a file is called a **module**. Definitions from a module can be 
imported into other modules or into the main module.

A module is a **file containing Python definitions and statements**.
The **file name is the module name** with the suffix `.py` appended.
Within a module, the module’s name (as a string) is available as the 
value of the global variable __name__. 

A module can contain executable statements as well as function definitions.
They are executed only the first time the module name is encountered in 
an import statement.


## Import Modules

Modules can import other modules.
It is customary but not required to place all import statements at the 
beginning of a module (or script, for that matter). 
The **imported module names are placed in the importing module’s global 
symbol table**.

_Example_: The import statement does not enter the names of the functions 
defined in fibo directly in the current symbol table. It **only enters the 
module name fibo** there. Using the module name you can access the functions.
```Python
import fibo

fibo.fib(1000)
```

_Example_: If the module name is followed by **as**, then the name following 
as is bound directly to the imported module.
This is effectively importing the module in the same way that import `fibo` 
will do, with the only difference of it being available as `fib`.
```Python
import fibo as fib
```

_Example_: There is a variant of the import statement that **imports names 
from a module directly** into the importing module’s symbol table.
```Python
from fibo import fib

fib(500)
```

_Example_: There is even a variant to **import all names** that 
a module defines.
```Python
from fibo import *

fib(500)
```

## Executing Modules as Scripts

When you run a Python module the code in the module will be executed, 
just as if you imported it, but with the __name__ set to "__main__".

We can make the file usable as a script as well as an importable module, 
because the code that parses the command line only runs if the module 
is executed as the “main” file:

```Python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
```
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34    
```

## Module Search Path
When a module named `spam` is imported, the interpreter first searches for 
a built-in module with that name. If not found, it then searches for a file 
named `spam.py` in a list of directories given by the variable **sys.path**. 

`sys.path` is initialized from these locations:

* The directory containing the input script (or the **current directory** 
    when no file is specified).

* **PYTHONPATH** (a list of directory names, with the same syntax as the 
    shell variable PATH).

* The installation-dependent default.

Python programs can modify `sys.path`.

The directory containing the script being run is placed at the beginning 
of the search path, ahead of the standard library path. 
This means that scripts in that directory will be loaded instead of modules 
of the same name in the library directory. 

## References
* [Modules](https://docs.python.org/3/tutorial/modules.html)

*Egon Teiniker, 2020-2025, GPL v3.0*
