# Setup Python

The following setup steps are described from the perspective of the [Debian VM](). 
For other platforms, the respective manuals must be used as an aid.

## Python 

Make sure that you have installed Python on your machine. If you use the Virtual Lab,
the following commands should work out of the box:
```
    $ python --version 
    Python 2.7.16

    $ python3 --version 
    Python 3.7.3

    $ sudo apt update
    $ sudo apt install python3-pip
    $ pip3 --version
    pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
```

Basically, we could work directly with the command line Python interpreter like:
```    
    $ python3
    Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
    [GCC 8.3.0] on linux 
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
$ pip3 install coverage
```

```
$ code .bashrc
    [i]
    
    export COVERAGE=/home/student/.local
    export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$M2_HOME/bin:$COVERAGE/bin:/opt/bin:$PATH
```
Now, start a new terminal (to activate your settings) and type:
```
$ coverage --version
Coverage.py, version 5.5 with C extension
Full documentation is at https://coverage.readthedocs.io
```




## References
* [https://www.python.org/](https://www.python.org/)

* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

*Egon Teiniker, 2020-2022, GPL v3.0*