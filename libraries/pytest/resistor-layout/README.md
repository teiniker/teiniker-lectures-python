## Project Layout 


```bash
├── src
│   └── parts
│       ├── __init__.py
│       └── resistor.py
└── test
    └── test_resistor.py
```


In order to make the project layout work in VS code, we have to add these lines 
to `settings.json`:

```json
{

  "python.analysis.extraPaths": [
    "${workspaceFolder}/src"
  ],

  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["test"]

}
```

## Run the Test Cases

```bash
$ pytest

============ test session starts ==============================================
platform linux -- Python 3.13.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/student/github/teiniker-lectures-python/libraries/pytest/resistor
collected 3 items           

test/test_resistor.py ...                                                 [100%]

============= 3 passed in 0.01s ================================================
```