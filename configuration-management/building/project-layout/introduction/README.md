# Python Project Layout 

A common Python project layout helps keep code organized, maintainable, 
and easy to distribute. While structures can vary slightly depending on 
the project (application vs. library), the layout below is widely used 
and considered best practice.


## Flat Layout

The flat layout refers to organising a project’s files in a folder or 
repository, such that the various configuration files and import packages 
are all in the top-level directory.

```bash
project/
│
├── README.md
├── pyproject.toml
│
├── main.py
├── module1.py
├── module2.py
│
└── test_module1.py
```

This approach works well for **small scripts and simple examples** because 
everything is located in one place and easy to understand at a glance. 
However, as the project expands, this flat structure quickly becomes difficult 
to manage. Files start to accumulate in the root directory, responsibilities 
blur, and it becomes harder to track dependencies and maintain clear boundaries 
between components.


## src Layout

The src layout deviates from the flat layout by moving the code that 
is intended to be importable (also known as import packages) into a 
subdirectory. This subdirectory is typically named `src/`.

```bash
project/
│
├── README.md
├── pyproject.toml
│
├── src/
│   └── project/
│       ├── __init__.py
│       ├── main.py
│       ├── module1.py
│       └── module2.py
│
├── tests/
│   ├── __init__.py
│   └── test_module1.py
│
├── docs/
│
└── bin/
```

* `README.md`: Describes the project and contains installation instructions.

* `pyproject.toml`: Defines project metadata and dependencies and is 
  used by packaging tools like `pip`.

* `src/`: This directory prevents accidental imports from the project root
    and it forces us to install the package before using it.
  - `__init__.py`: Marks directory as a Python package.
  - `main.py`: Entry point
  - `module1.py`, `module2.py`: Application logic

* `tests/`: Contains unit and integration tests, usually uses **pytest** 
  or **unittest**.  

* `docs/`: Documentation files which can be built using tools like **Sphinx**.

* `bin/`: Utility scripts, e.g. deployment helpers, data processing scripts, etc.


## Running Tests

With a src layout, Python does not automatically know that `src/` 
should be on the import path.
Therefore, when pytest runs, it may fail.

There are different ways to make pytest find the parts package...


### Configure pytest 

Create a `pytest.ini` file in the project root:

```ini
[pytest]
pythonpath = src
testpaths = test
```

With this configuration file in place, we can run our test cases:

```bash
$ pytest
```


### Install the Package in Editable Mode

This approach requires a `pyproject.toml` file so Python knows how 
to install the package.

_Example:_ Minimal `pyproject.toml` file

```toml
[project]
name = "parts"
version = "0.0.1"

[tool.setuptools.packages.find]
where = ["src"]
```

Now we can install the package in editable mode.

From the project root:

```bash
$ pip install -e .
$ pytest
```

This approach has many advantages:
* Mimics real usage
* Works reliably in CI/CD
* Scales for large projects


### Configure VS Code 

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



## References 

* [Real Python: project layout](https://realpython.com/ref/best-practices/project-layout/)

* [Python Packaging User Guide: src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)


*Egon Teiniker, 2020-2026, GPL v3.0*
