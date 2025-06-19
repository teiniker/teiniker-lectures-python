# JSON Files

The JavaScript Object Notation (JSON) file format is a lightweight data-interchange
format that is easy for humans to read and write, as well as for machines to parse
and generate.

It is **text-based**, completely language-independent, and uses conventions familiar
to programmers of the C-family of languages, which includes C, C++, Java, Python,
and many others. This has made JSON a popular choice for data interchange on the web,
including configurations, **RESTful API responses**, and more.

Here are the key syntax elements of JSON:
* **Objects** are enclosed in curly braces **{}** and represent a **collection
    of key/value pairs**. Each name is followed by a colon (:) and
    the name/value pairs are separated by commas.
* **Arrays** are enclosed in square brackets **[]** and represent an
    **ordered list of values**, separated by commas.
* **Values** can be strings (in double quotes), numbers, objects, arrays,
    true, false, or null.
* **Strings** are a sequence of zero or more Unicode characters, wrapped in
    double quotes, using backslash escapes.
* **Numbers** are similar to those in most programming languages, and can
    be integers, fractions, or use exponent notation.

_Example_: JSON data with headers
```
[
    {
        "id":1,
        "temperature":24.5,
        "humidity":65.2
    },
    {
        "id":2,
        "temperature":22.1,
        "humidity":55.8
    }
]
```

While JSON is not the most compact data format, its balance between readability
and simplicity often makes it an ideal choice for many applications.

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


## json Module

The `json` module in Python provides functionalities for working with 
**JSON (JavaScript Object Notation)** data. It allows you to encode Python 
objects into JSON strings and decode JSON strings into Python objects. 

The `json` module is part of the Python standard library, so you don't 
need to install any additional packages to use it. 
It is a versatile tool for working with JSON data, allowing you to exchange 
information between different programming languages or interact with 
JSON-based APIs.

Here's a summary of the key functionalities provided by the json module:

* **JSON Encoding (json.dumps())**: The `dumps()` function converts a Python 
    object into a JSON-formatted string. It supports various parameters to 
    control the encoding process, such as specifying the indentation level, 
    sorting keys, and handling custom objects.

* **JSON Decoding (json.loads())**: The `loads()` function converts a 
    JSON-formatted string into a corresponding Python object. It parses 
    the JSON string and constructs the appropriate Python data structures, 
    such as dictionaries, lists, strings, numbers, booleans, and `None`.

* **File I/O (json.dump() and json.load())**: The `dump()` function serializes 
    a Python object and writes it to a file as JSON data. It is useful when you 
    want to save JSON data to a file. 
    
    Conversely, the `load()` function reads JSON data from a file and converts 
    it into a Python object.

* **Serialization and Deserialization**: JSON encoding and decoding are collectively 
    referred to as serialization and deserialization. Serialization is the process 
    of converting a Python object into a JSON string, while deserialization is the 
    reverse process of converting a JSON string into a Python object.

* **Error Handling (json.JSONDecodeError)**: The `JSONDecodeError` exception is 
    raised when there is an error during JSON decoding. It provides information 
    about the specific location and reason for the decoding error, such as invalid 
    JSON syntax or mismatched data types.

When we parse a JSON file using Python’s built-in json module, the data is 
typically loaded into a **nested structure of dictionaries and lists**, 
depending on the structure of the JSON.

| JSON Type | Python Type     |
| --------- | --------------- |
| Object    | `dict`          |
| Array     | `list`          |
| String    | `str`           |
| Number    | `int` / `float` |
| Boolean   | `bool`          |
| null      | `None`          |

_Example:_ Parsing JSON data

```
{
    'person': 
        {
            'name': 'John', 
            'age': 30, 
            'city': 'Graz'
        }
}
```

```Python
person = data['person']
print(person)   # {'name': 'John', 'age': 30, 'city': 'Graz'}

name = person['name']
print(name)     # John

age = person['age']
print(age)      # 30

city = person['city']
print(city)     # Graz
```


## References
* [Youtube (Corey Schafer): Working with JSON Data using the json Module](https://youtu.be/9N6a-VLBa2I)

* [Working With JSON Data in Python](https://realpython.com/python-json/)
* [The Python Standard Library: JSON Encoder and Decoder](https://docs.python.org/3/library/json.html)
* [RFC7159: The JavaScript Object Notation (JSON) Data Interchange Format](https://datatracker.ietf.org/doc/html/rfc7159.html)

*Egon Teiniker, 2020-2025, GPL v3.0*
