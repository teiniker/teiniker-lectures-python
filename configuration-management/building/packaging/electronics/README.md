# Example: Python Packaging - electronics

Create the following project structure:

```bash
.
├── pyproject.toml
├── README.txt
├── src
│   └── electronics
│       ├── __init__.py
│       └── parts.py
└── test
    └── resistor_test.py
```

## Build Source and Wheel Distributions 

```bash
$ python -m build --sdist .
$ python -m build --wheel .

dist/
├── electronics-0.1.0-py3-none-any.whl
└── electronics-0.1.0.tar.gz
```


## Use Package in a Unit Test  

```bash 
$ cd test
$ python3 -m venv .venv
$ source .venv/bin/activate

$ pip install ../dist/electronics-0.1.0-py3-none-any.whl
$ pip list
Package     Version
----------- -------
electronics 0.1.0
pip         25.1.1

$ python resistor_test.py
```


## Build Bytecode Distribution 

Compile the .py files into .pyc files:

```bash
$ python -m pyc_wheel dist/electronics-0.1.0-py3-none-any.whl

$ unzip -l dist/electronics-0.1.0-py3-none-any.whl
Archive:  dist/electronics-0.1.0-py3-none-any.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2025-10-08 13:17   electronics/
        0  2025-10-08 13:17   electronics-0.1.0.dist-info/
      471  2025-10-08 13:17   electronics-0.1.0.dist-info/RECORD
       12  2025-10-08 11:11   electronics-0.1.0.dist-info/top_level.txt
       92  2025-10-08 13:17   electronics-0.1.0.dist-info/WHEEL
      159  2025-10-08 11:11   electronics-0.1.0.dist-info/METADATA
     1737  2025-10-08 13:17   electronics/parts.pyc                     <==
      140  2025-10-08 13:17   electronics/__init__.pyc                  <==    
---------                     -------
     2611                     8 files
```

Run the tests to see if this is working.

*Egon Teiniker, 2025, GPL v3.0*