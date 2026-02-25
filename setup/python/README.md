# Setup Python

The following setup steps are described from the perspective of the [Debian VM]().
For other platforms, the respective manuals must be used as an aid.

## Python

Make sure that you have installed Python on your machine. If you use the Virtual Lab,
the following commands should work out of the box:
```
    $ python --version
    Python 3.13.5

    $ pip --version
    pip 25.1.1 from /usr/lib/python3/dist-packages/pip (python 3.13)
```

Basically, we could work directly with the command line Python interpreter like:
```
    $ python
    Python 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hello world!')
    Hello world!
    >>> exit()
```
But for more sophisticated examples we use a more comfortable editor ...


## Coverage.py
Coverage.py is a tool for **measuring code coverage** of Python programs.

It monitors your program, noting which parts of the code have been executed,
then analyzes the source to identify code that could have been executed but
was not.
```
$ pip install coverage
```

```
$ code .bashrc
    export PYTHON_LOCAL=/home/student/.local
    export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$M2_HOME/bin:$PYTHON_LOCAL/bin:/opt/bin:$PATH
```
Now, start a new terminal (to activate your settings) and type:
```
$ coverage --version
Coverage.py, version 7.6.12 with C extension
```




## References
* [https://www.python.org/](https://www.python.org/)

* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

*Egon Teiniker, 2020-2025, GPL v3.0*
