# CSV Files

The Comma Separated Values (CSV) file format is a simple, widely used format for
storing **tabular data** (data that is structured into rows and columns).
As the name implies, in a CSV file, commas are typically used to separate individual
fields within a record. Here are the key characteristics and details about the CSV format:

* **Structure**: A CSV file consists of lines of text, where each line represents a single
    record or row in a table. Each field within a record is separated by a comma,
    although other delimiters (like semicolons or tabs) can also be used, depending
    on the context and settings of the software being used.

* **Headers**: The first line of a CSV file often contains headers, which are
    the **names of the columns in the table**. These headers provide context for the
    data in each column but are not mandatory.

* **Data Types**: CSV files **do not distinguish data types**. All data is stored as
    strings. Any interpretation of the data type (e.g., as integers, floating-point numbers,
    or dates) must be done by the software reading the CSV data.

* **Quoting**: To handle cases where data values themselves contain commas or
    other special characters (like newline characters or the delimiter itself),
    CSV files often enclose the fields in quotes. The most common quoting character
    is the **double-quote (")**.


The **simplicity of the CSV format** makes it easy to create, edit, and manipulate with
basic text editors, spreadsheet programs like Microsoft Excel or Google Sheets, and
programming languages that can read and write text files. This simplicity also ensures
high compatibility across different systems and software.

While the basic concept of CSV is straightforward, there is a notable **lack
of standardization** regarding specific implementation details (e.g., handling of
special characters, encodings, newline characters).
This can lead to issues when exchanging CSV files between different systems or
programs. To mitigate these issues, some conventions and more detailed formats
(like **RFC 4180**) have been proposed to standardize CSV usage.

_Example_: CVS data with headers
```
id,temperature,humidity
1,24.5,65.2
2,22.1,55.8
3,26.7,70.3
4,21.9,60.1
5,23.4,68.7
6,25.1,71.9
7,27.3,74.2
8,20.4,50.5
9,28.9,80.3
10,22.7,57.1
```


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

## References

* [Youtube (Corey Schafer): CSV Module - How to Read, Parse, and Write CSV Files](https://youtu.be/q5uM4VKywbA)
* [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)
* [The Python Standard Library: CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
* [RFC4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180.html)

*Egon Teiniker, 2020-2025, GPL v3.0*
