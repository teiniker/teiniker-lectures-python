# Example: Resistor Layout 

This example adopts a **src layout** to structure and isolate 
the Python source code in a clear and maintainable way. 

Instead of placing modules directly in the project root, all 
application code is stored inside a dedicated `src/` directory. 

This approach creates a cleaner separation between the package 
itself and other project files such as configuration, and tests.

```bash
├── src
│   └── parts
│       ├── __init__.py
│       └── resistor.py
└── test
    └── test_resistor.py
```

With a src layout, Python does not automatically know that `src/` 
should be on the import path.
Therefore, when pytest runs, it may fail.

There are different ways to make pytest find the parts package...


## Configure pytest 

Create a pytest.ini file in the project root:

```ini
[pytest]
pythonpath = src
testpaths = test
```

## Configure VS Code 

In order to make the src layout work in VS code, we have to add 
these lines to `settings.json`:

```json
{

  "python.analysis.extraPaths": [
    "${workspaceFolder}/src"
  ],

  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["test"]

}
```

## Run Test Cases

```bash
$ pytest

============ test session starts ==============================================
platform linux -- Python 3.13.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/student/github/teiniker-lectures-python/libraries/pytest/resistor
collected 3 items           

test/test_resistor.py ...                                                 [100%]

============= 3 passed in 0.01s ================================================
```



*Egon Teiniker, 2020-2026, GPL v3.0*
