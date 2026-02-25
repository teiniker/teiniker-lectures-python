# Python Packaging 

Publishing a package requires a flow from the author’s source code to an end 
user’s Python environment. 

The steps to achieve this are:

* Have a **source tree containing the package**. 
    This is typically a checkout from a version control system (VCS).

* Prepare a configuration file describing the **package metadata**
    (name, version and so forth) and how to create the build artifacts. 
    For most packages, this will be a **pyproject.toml** file, maintained 
    manually in the source tree.

* **Create build artifacts** to be sent to the package distribution service. 
    These will normally be a **source distribution (sdist)** 
    and one or more **built distributions (wheels)**. 
    These are made by a build tool using the configuration file from the 
    previous step. Often there is just one generic wheel for a pure Python package.

* Upload the build artifacts to the **package distribution service** (usually PyPI).


To use the package, end users must:

* **Download** one of the package’s build artifacts from the package distribution 
    service.

* **Install it in their Python environment**, usually in its site-packages directory. 
    This step may involve a build/compile step which, if needed, must be described by 
    the package metadata.

These last 2 steps are typically performed by `pip` when an end user runs **pip install**.



## Create a Python Package 


### Source Tree 

The source tree contains the package source code.
The particular version of the code used to create the build artifacts will typically 
be a checkout from git based on a tag associated with the version.

_Example:_ Simple algorithm implementation.
```bash
algorithm
├── README.md
├── pyproject.toml
└── src
    └── algorithm
        ├── fibonacci.py
        └── __init__.py
```    


### Configuration File

The configuration file depends on the tool used to create the build artifacts.

At a minimum, the `pyproject.toml` file needs a `[build-system]` table specifying your build tool. 

The particular build tool you choose dictates what additional information 
is required in the `pyproject.toml` file. For example, we might specify:

* A [project] table containing project Core Metadata (name, version, author and so forth),

* A [tool] table containing tool-specific configuration options.


_Example:_ Configuration file using wheel

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "simple_lib"
version = "0.1.0"
description = "Simple Algorthm Library"
readme = { file = "README.md", content-type = "text/markdown" }
authors = [{ name = "homer", email = "homer@springfield.com" }]
requires-python = ">=3.8"
dependencies = []

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

* `[build-system]`
    - `requires`: install setuptools ≥ 69 and wheel into the isolated env before building.
    - `build-backend`: use setuptools’ backend (setuptools.build_meta) to create 
        the sdist (source tarball) and wheel (built distribution).

* `[project]`
    - `name`: the package’s distribution name on PyPI (`simple_lib`). This is what users will `pip install`.
    - `version`: static version string (you can later switch to dynamic versioning, e.g. `setuptools_scm`).
    - `description`: short summary 
    - `readme`: points to `README.md` and declares its content type for PyPI’s project page rendering.
    - `authors`: metadata for packaging indexes and tools.
    - `requires-python`: declares interpreter compatibility; installers can skip incompatible environments.
    - `dependencies`: runtime requirements (empty here). If you needed, say, NumPy: ["numpy>=2"].

* `[tool.setuptools]`
    - `package-dir = { "" = "src" }`: tells setuptools that the root package directory is `src/`.
    
*  `[tool.setuptools.packages.find]`
    - where = ["src"]: asks setuptools to discover packages by scanning `src/` for directories containing 
        `__init__.py`.


### Build Package

Before building your package, ensure the necessary tools are installed (use a virtual environment):

```bash
$ pip install build twine
```

- `build` is used to create source and wheel distributions.
- `twine` is used to upload distributions to PyPI and verify them.

* **The source distribution (sdist)**:
A source distribution contains enough to install the package from source 
in an end user’s Python environment. As such, it needs the package source, 
and may also include tests and documentation. 
These are useful for end users wanting to develop your sources, and for 
end user systems where some local compilation step is required (such as 
a C extension).

The build package knows how to invoke your build tool to create one of these:
```bash
$ python -m build --sdist source-tree-directory
```

* **The built distributions (wheels)**:

A built distribution contains only the files needed for an end user’s Python 
environment. No compilation steps are required during the install, and the 
**wheel file** can simply be unpacked into the site-packages directory. 
This makes the install faster and more convenient for end users.

A pure Python package typically needs only one “generic” wheel. 

A package with compiled binary extensions needs a wheel for each supported 
combination of Python interpreter, operating system, and CPU architecture 
that it supports. 
If a suitable wheel file is not available, tools like `pip` will fall back 
to installing the source distribution.

The build package knows how to invoke your build tool to create one of these:

```bash
$ python -m build --wheel source-tree-directory
```


_Example:_ Build a source and wheel package and check the distributions 
```bash
$ cd algorithm 
$ python -m build --sdist .
$ python -m build --wheel .

├── dist
│   ├── simple_lib-0.1.0-py3-none-any.whl
│   └── simple_lib-0.1.0.tar.gz
```

### Build Bytecode Package

If you do not want to distribute the Python source code together with the package, 
you can **compile it to bytecode** beforehand.  

Note that this bytecode can only be used with a **specific Python version**!

```bash
$ pip install pyc-wheel
```

We can convert a regular wheel file to bytecode with the following command:

```bash
$ python -m pyc_wheel dist/simple_lib-0.1.0-py3-none-any.whl 
Listing '/tmp/tmpkhaigb9_'...
Listing '/tmp/tmpkhaigb9_/algorithm'...
Compiling '/tmp/tmpkhaigb9_/algorithm/__init__.py'...
Compiling '/tmp/tmpkhaigb9_/algorithm/fibonacci.py'...
Listing '/tmp/tmpkhaigb9_/simple_lib-0.1.0.dist-info'...
Deleting py file: /tmp/tmpkhaigb9_/algorithm/fibonacci.py
Deleting py file: /tmp/tmpkhaigb9_/algorithm/__init__.py
```

To verify the result of this transformation, unzip the wheel file in a 
temporary directory:

```bash
$ mkdir tmp
$ cd tmp/
$ unzip ../simple_lib-0.1.0-py3-none-any.whl
Archive:  ../simple_lib-0.1.0-py3-none-any.whl
   creating: algorithm/
   creating: simple_lib-0.1.0.dist-info/
  inflating: simple_lib-0.1.0.dist-info/RECORD  
  inflating: simple_lib-0.1.0.dist-info/top_level.txt  
  inflating: simple_lib-0.1.0.dist-info/WHEEL  
  inflating: simple_lib-0.1.0.dist-info/METADATA  
  inflating: algorithm/fibonacci.pyc  
  inflating: algorithm/__init__.pyc  
```
As we can see, the original `.py` source files have been removed from the wheel 
and replaced with `.pyc` bytecode files. This ensures that only compiled bytecode 
is distributed, protecting the source code while still allowing the package to 
be installed and used with the compatible Python version.



### Upload to the Package Distribution Service

For our initial experiments, it is sufficient to store the package files locally.

## Install and Use a Python Package 

Now that the package is published, end users can download and install the package into 
their Python environment. Typically this is done with **pip**. 

_Example:_ Install from a local wheel file

1. Create a virtual environment:

```bash 
$ cd app
$ python3 -m venv .venv
$ source .venv/bin/activate
```

2. Install the wheel file:

```bash 
$ pip install ../dist/simple_lib-0.1.0-py3-none-any.whl
$ pip list
Package    Version
---------- -------
pip        25.1.1
simple_lib 0.1.0
```

3. Run the application:

```bash
$ python demo.py
```

4. Deactivate virtual environment:
```bash
$ deactivate
```




## References
* [The Packaging Flow](https://packaging.python.org/en/latest/flow/)

* [RealPython: What Are Python Wheels and Why Should You Care?](https://realpython.com/python-wheels/)

* [wheel documentation](https://wheel.readthedocs.io/en/stable/)


*Egon Teiniker, 2020-2026, GPL v3.0*
