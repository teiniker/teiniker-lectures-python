# Text Files

A **file** is a contiguous set of bytes used to store data. 
This data is organized in a specific format and can be anything as simple as a text file or as complicated as 
a program executable.
What this data represents depends on the format specification used, which is typically represented by an **extension**.

When we access a file on an operating system, a **file path** is required. 
The file path is a string that represents the location of a file. 
It’s broken up into three major parts:
* **Folder Path**: The file folder location on the file system where subsequent folders are separated by a forward 
    slash `/` (Unix) or backslash `\` (Windows)
* **File Name**: The actual name of the file
* **Extension**: the end of the file path pre-pended with a period `.` used to indicate the file type

We can also use the special characters **double-dot** `..` to move one directory up. 
The double-dot `..` can be chained together to traverse multiple directories above the current directory.


## Opening and Closing Files

When you want to work with a file, the first thing to do is to open it. 
This is done by invoking the `open()` built-in function. 
`open()` has a single required argument that is the path to the file. 
`open()` has a single return, the **file object**.

It’s important to remember that it’s our responsibility to close the file.
There are two ways that we can use to ensure that a file is closed properly, even when encountering an error:
* The first way to close a file is to use the **try-finally** block:
    ```Python
    file = open('data.txt')
    try:
        # File processing 
    finally:
        file.close()
    ```

* The second way to close a file is to use the **with** statement:
    ```Python
    with open('data.txt') as file:
        # File processing 
    ```
    The with statement automatically takes care of closing the file once it leaves the 
    with block, even in cases of error.

We will also want to use the second positional argument, **mode**. 
This argument is a string that contains multiple characters to represent how you want to open the file. 
The default and most common is `'r'`, which represents opening the file in read-only mode as a text file:
```Python
    with open('data.txt', 'r') as file:
        # File processing 
```
The most common options are:
* `'r'`   Open for reading (default)
* `'w'`   Open for writing, truncating (overwriting) the file first
* `'a'`   Open for writing, appending to the end of the file if it exists
* `'rb'` or `'wb'` Open in binary mode (read/write using byte data)


## Reading and Writing Files

Once we have opened up a file, we can read or write to the file. 
There are multiple methods that can be called on a file object:
* `read(size=-1)`\
    Reads from the file based on the number of size bytes. 
    If no argument is passed or None or -1 is passed, then the entire file is read.

* `readline(size=-1)`\
    Reads at most size number of characters from the line. 
    This continues to the end of the line and then wraps back around. 
    If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.

* `readlines()`\
    Reads the remaining lines from the file object and returns them as a list.

_Example_: Reading a file line by line
```Python
file = open('data.txt')
for line in file:
    print("> {}".format(line), end='')
file.close()
```

As with reading files, file objects have multiple methods that are useful for **writing to a file**:
* `write(string)`\
    Writes the string to the file.

* `writelines(seq)`\
    Writes the sequence to the file. 
    No line endings are appended to each sequence item. 
    It’s up to us to add the appropriate line ending(s).

_Example_: Writing into a file 
```Python
with open('tmp.txt','w') as out_file:
    out_file.writelines(data)
```

## References

* Eric Matthes. **Python Crash Course**. No Starch Press,
    Chapter 10: Files and Exceptions
    
* [Youtube (Corey Schafer): File Objects - Reading and Writing to Files](https://youtu.be/Uh2ebFW8OYM)
* [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
* [The Python Tutorial: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

*Egon Teiniker, 2020-2025, GPL v3.0*
