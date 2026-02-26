# Example: Resistor Layout 

This example adopts a **src layout** to structure and isolate 
the Python source code in a clear and maintainable way. 

Instead of placing modules directly in the project root, all 
application code is stored inside a dedicated `src/` directory. 

This approach creates a cleaner separation between the package 
itself and other project files such as configuration, and tests.

```bash
├── pytest.ini
├── src
│   └── parts
│       ├── __init__.py
│       └── resistor.py
└── test
    └── test_resistor.py
```


Thanks to the configuration in the `pytest.ini` file, we can 
run the tests without any problems:

```bash
$ pytest
```


*Egon Teiniker, 2020-2026, GPL v3.0*
