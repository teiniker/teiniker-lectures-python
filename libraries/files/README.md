# File Handling

One of the most common tasks that you can do with Python is reading and writing files. 
Whether it’s writing to a simple text file, reading a complicated server log, or even analyzing raw byte data, 
all of these situations require reading or writing a file.

## File

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


## Opening and Closing a File

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

# CSV Files

A **Comma Separated Values (CSV)** file is a type of plain text file that uses specific structuring to arrange 
tabular data. 
Because it’s a plain text file, it can contain only actual text data—in other words, printable ASCII or Unicode characters.

CSV files are normally created by programs that **handle large amounts of data**. 
They are a convenient way to export data from spreadsheets and databases as well as import or use it in other programs.

CSV files are very easy to work with programmatically. 
Any language that supports text file input and string manipulation (like Python) can work with CSV files directly.

_Example_: CSV file
```
    1,0.8273
    2,0.7822
    3,0.9731
    4,0.1239
    5,0.9898
``` 
In general, the separator character is called a **delimiter**, and the comma is not the only one used. 
Other popular delimiters include the tab `\t`, colon `:` and semi-colon `;` characters.

## Reading CSV Files

The **csv library** provides functionality to both read from and write to CSV files. 
Designed to work out of the box with Excel-generated CSV files, it is easily adapted to work with a variety 
of CSV formats. 
The csv library contains objects and other code to read, write, and process data from and to CSV files.

The CSV file is opened as a text file with Python’s built-in `open()` function, which returns a file object. 

_Example_: Read from a CSV file
```Python
with open('data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        print('line: {} data: {}'.format(row[0], row[1]))
```
Each row returned by the reader is a list of String elements containing the data found by removing the delimiters. 

The `reader` object can handle different styles of CSV files by specifying additional parameters, 
some of which are shown below:
* `delimiter` specifies the character used to separate each field. The default is the comma `','`.
* `quotechar` specifies the character used to surround fields that contain the delimiter character. 
    The default is a double quote `' " '`.
* `escapechar` specifies the character used to escape the delimiter character, in case quotes aren’t used. 
    The default is no escape character.

## Writing CSV Files 

You can also write to a CSV file using a `writer` object and the `write_row()` method.

_Example_: Write into a CSV file
```Python
with open('tmp.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerow([0, 3.14159, "PI"])
```

Whether quoting is used or not is determined by the `quoting` optional parameter:
* `csv.QUOTE_MINIMAL`: Quote fields only if they contain the delimiter or the quotechar. 
    This is the default case.
* `csv.QUOTE_ALL`: Quote all fields.
* `csv.QUOTE_NONNUMERIC`: Quote all fields containing text data and convert all numeric fields to the float data type.
* `csv.QUOTE_NONE`: Escape delimiters instead of quoting them. 
    In this case, we also must provide a value for the `escapechar` optional parameter.

# JSON Files

**JavaScript Object Notation (JSON)** was inspired by a subset of the JavaScript programming language dealing 
with object literal syntax.
JSON has long since become language agnostic and exists as its own standard
The community at large adopted JSON because it’s easy for both humans and machines to create and understand.

_Example_: JSON file
```
    {
      "person":
        {
          "name": "John",
          "age": 30,
          "city": "Graz"
        }
    }
``` 
JSON supports primitive types, like strings and numbers, as well as nested lists and objects.

The process of encoding JSON is usually called **serialization**. 
This term refers to the transformation of data into a series of bytes (hence serial) to be 
stored or transmitted across a network. 

**Deserialization** is the reciprocal process of decoding data that has been stored or delivered 
in the JSON standard.

## Reading from JSON Files

Python comes with a built-in package called `json` for encoding and decoding JSON data.
In this `json` library, we will find `load()` and `loads()` (pronounced as “load-s”) for turning JSON 
encoded data into Python objects.

_Example_: Read from a JSON file
```Python
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```
Things are pretty straightforward here, but keep in mind that the result of this method could return different
data types.
In most cases, the root object will be a `dict` or a `list`. 


## Writing into JSON Files
The `json` library exposes the `dump()` method for writing data to files. 
There is also a `dumps()` method for writing to a Python string.

Simple Python objects are translated to JSON according to a fairly intuitive conversion.

_Example_: Write into a JSON file
```Python
with open('tmp.json', 'w') as file:
    json.dump(data, file, indent=4)
```
Note that `dump()` takes two positional arguments: 
* The `data` object to be serialized
* The `file` object to which the bytes will be written

We can use the `indent` keyword argument to specify the indentation size for nested structures.


## References
**File Handling**
* Eric Matthes. **Python Crash Course**. No Starch Press,
    Chapter 10: Files and Exceptions
    
* [Youtube (Corey Schafer): File Objects - Reading and Writing to Files](https://youtu.be/Uh2ebFW8OYM)
* [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
* [The Python Tutorial: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

**CSV Files**
* [Youtube (Corey Schafer): CSV Module - How to Read, Parse, and Write CSV Files](https://youtu.be/q5uM4VKywbA)
* [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)
* [The Python Standard Library: CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

**JSON Files**
* [Youtube (Corey Schafer): Working with JSON Data using the json Module](https://youtu.be/9N6a-VLBa2I)
* [Working With JSON Data in Python](https://realpython.com/python-json/)
* [The Python Standard Library: JSON Encoder and Decoder](https://docs.python.org/3/library/json.html)

*Egon Teiniker, 2020-2025, GPL v3.0*

