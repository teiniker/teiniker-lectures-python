# Binary Files

A **binary file** stores data as a sequence of raw bytes.

Unlike a text file, the content is not interpreted as characters 
using a text encoding such as UTF-8.

This makes binary files suitable for data formats such as images, 
audio files, serialized objects, compressed archives, or arbitrary 
byte streams.

Just like text files, binary files are identified by a **file path** 
and usually by a file extension. In this example, the file `data.bin` 
contains a sequence of bytes.

If we open such a file in a text editor, the content is typically 
not human-readable because the bytes do not necessarily represent 
printable characters.


## Opening and Closing Binary Files

When working with a binary file, we still use the built-in `open()` 
function.

The main difference is the **mode**:
* `'rb'` opens a file for reading in binary mode
* `'wb'` opens a file for writing in binary mode
* `'ab'` opens a file for appending in binary mode

As with text files, it is important to close the file properly.
The preferred way is to use the **with** statement, which automatically 
closes the file when leaving the block:

```Python
with open('data.bin', 'rb') as in_file:
    data = in_file.read()
    print(data)
```

Here, the file is opened in **read-binary mode**.

The call to `read()` returns the complete file content as a `bytes` object.
Printing this object shows the byte values, for example `b'\x00\x01\x02...'`.


## Reading and Writing Binary Files

Once a binary file has been opened, we can read or write raw bytes.
The API is similar to text files, but the data type is different:

* `read(size=-1)`\
    Reads up to `size` bytes from the file.
    If no size is given, the whole file is read and returned as 
    a `bytes` object.

* `write(bytes)`\
    Writes a `bytes` object to the file and returns the number 
    of bytes written.

_Example_: Reading from one binary file and writing the same bytes 
into another file

```Python
with open('data.bin','rb') as in_file:
    data = in_file.read()
    print(data)

with open('tmp.bin','wb') as out_file:
    out_file.write(data)
```

In this example:
* `in_file.read()` reads all bytes from `data.bin`
* the variable `data` contains a `bytes` object
* `out_file.write(data)` writes the same bytes unchanged 
    to `tmp.bin`

This is a typical use case for binary files because the content 
should usually be copied exactly without any encoding or 
line-ending conversion.


## References

* Eric Matthes. **Python Crash Course**. No Starch Press,
    Chapter 10: Files and Exceptions
    
* [Youtube (Corey Schafer): File Objects - Reading and Writing to Files](https://youtu.be/Uh2ebFW8OYM)
* [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
* [The Python Tutorial: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

*Egon Teiniker, 2020-2026, GPL v3.0*
