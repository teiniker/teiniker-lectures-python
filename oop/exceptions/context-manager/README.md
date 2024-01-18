# Context Manager 

A context manager is a Python object that is used to **manage the resources** used by a block of code, 
such as a file, a database connection, or a network socket.

In Python, the `with` statement is used to ensure that we never leave any resource open.

The `TextReader` class defines a context manager for reading a text file. 
The `__init__` method initializes the class with the filename, and sets the file 
attribute to None.

```Python
class TextReader:
    def __init__(self, filename:str)->None:
        self.filename = filename
        self.file = None

    def __enter__(self):
        print(f"open file: {self.filename}")
        self.file = open(self.filename, 'r', encoding="utf-8")
        return self.file

    def __exit__(self, *args):
        print(f"close file: {self.filename}")
        self.file.close()
```

The `__enter__` method is called when the **context is entered**, which in 
this case means when the `with` statement is executed. 
This method opens the file with the specified filename using the `open()` function, 
and returns the file object. 
The encoding parameter is set to `utf-8` to ensure that the file is read as a 
`UTF-8` encoded text file.

The `__exit__` method is called when the **context is exited**, which means when 
the block of code inside the with statement is executed, or when an exception is 
raised. This method closes the file using the `close()` method.

When the `with` statement is used with an instance of the `TextReader` class, 
the `__enter__` method is called, and the file object returned by this method is 
used in the block of code inside the with statement. 
When the block of code is completed, the `__exit__` method is called to close 
the file, even if an exception occurred.

```Python
with TextReader("data.txt") as txt_file:
    data = txt_file.read()
    print(data)
```

Fortunately, there is already a context manager for files we can use:

```Python
with open('data.txt', 'r', encoding="utf-8") as txt_file:
    data = txt_file.read()
    print(data)
```


## Resources
* [YouTube (Corey Schafer): Context Managers - Efficiently Managing Resources](https://youtu.be/-aKFBoZpiqA)

*Egon Teiniker, 2020-2023, GPL v3.0*