# Analyze a Python Package: numpy

Instead of using a single command to install the numpy package:

```bash
$ pip install numpy
```

We want to download the source and built distributins and analyze their content: 


1. Download numpy packages from PyPi:

    Visit the [numpy PyPI page](https://pypi.org/project/numpy/#files) to view available distributions.

    Download both the source distribution (`.tar.gz`) and a built wheel (`.whl`) for your platform:

    After downloading, you can list the files to verify:

    ```bash
    $ ll
    total 34180
    -rw-rw-r-- 1 student student 14420354 Sep 30 15:49 numpy-2.3.3-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl
    -rw-rw-r-- 1 student student 20576648 Sep 30 15:47 numpy-2.3.3.tar.gz
    ```

    _Note:_ Usually, there is a single source distribution (`.tar.gz`), but 
    multiple built distributions (`.whl` files) are provided—each targeting 
    different platforms (operating systems, architectures) and Python versions. 
    This allows users to install a pre-built package optimized for their 
    specific environment.


2. Unzip the source distribution: 

    ```bash
    $ mkdir tmp-source
    $ cd tmp-source/
    $ tar xvzf ../numpy-2.3.3.tar.gz
    ```

    This extracts the full source tree of numpy, including all Python modules, 
    C source files, build scripts, and documentation. You can now inspect the 
    original source code and project structure as distributed by the maintainers.

3. Unzip a built distribution:

    ```bash
    $ mkdir tmp-built
    $ cd tmp-built/
    $ unzip ../numpy-2.3.3-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl
    ```

    In the extracted contents, we will find shared libraries (compiled C extensions) 
    alongside Python source files. 
    
    The C code is pre-built for a specific platform and architecture, while 
    the Python files are typically plain `.py` files that will be compiled 
    to bytecode (`.pyc`) by the Python interpreter at runtime.


*Egon Teiniker, 2025, GPL v3.0*