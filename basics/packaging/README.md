# Python Packaging 

## Build a Wheel File 
Given the following project structure:

```
├── pyproject.toml
├── README.md
└── src
    └── algorithm
        ├── fibonacci.py
        └── __init__.py
```


Build the package and check the distributions 
```bash 
$ python -m build

├── dist
│   ├── simple_lib-0.1.0-py3-none-any.whl
│   └── simple_lib-0.1.0.tar.gz

$ python -m twine check dist/*
```

## Install and Use a Local Wheel File 

Create a virtual environment:

```bash 
$ cd app
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Install the wheel file:

```bash 
$ pip install ../dist/simple_lib-0.1.0-py3-none-any.whl
$ pip list
```

Run the application:

```bash
$ cd app 
$ python demo.py
```

Deactivate virtual environment:
```bash
$ deactivate
```



