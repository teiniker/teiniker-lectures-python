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


## References

* [Python Standard Library: JSON encoder and decoder](https://docs.python.org/3/library/json.html)

*Egon Teiniker, 2020-2023, GPL v3.0*