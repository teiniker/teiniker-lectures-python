# Types in Python

Objects are Python’s abstraction for data. All data in a Python program is
represented by objects or by relations between objects.

Every object has an **identity**, a type and a value.
An object’s identity never changes once it has been created; you may think of
it as the object’s address in memory. The `is` operator compares the identity
of two objects; the `id()` function returns an integer representing its identity.

An object’s **type** determines the operations that the object supports and also
defines the possible values for objects of that type. The `type()` function returns
an object’s type. An object’s type is also unchangeable.

The value of some objects can change. Objects whose value can change are said to
be **mutable**. 
Objects whose value is unchangeable once they are created are called **immutable**.
An object’s mutability is determined by its type; for instance, numbers, strings 
and tuples are immutable, while dictionaries and lists are mutable.
If an immutable container (like a tuple) contains a reference to a mutable object,
its value changes if that mutable object is changed.

Objects are never explicitly destroyed; however, when they become unreachable they
may be **garbage-collected**.


## Numbers
The **integer numbers** (e.g. 2, 4, 20) have type `int`, the ones with a fractional 
part (e.g. 5.0, 1.6) have type **float**.
Division `/` always returns a `float`.
To do floor division and get an integer result you can use the `//` operator;
to calculate the remainder you can use `%` It is possible to use the `**` operator 
to calculate powers.

_Example:_ Number operations
```Python
a = 10
b = 3

assert a + b == 13
assert a - b == 7
assert a * b == 30
c = 10/3
print(c)
assert a // b == 3
assert a % b == 1
assert a ** b == 1000
```

## Strings
Python can also manipulate strings, which can be expressed in several ways.
They can be enclosed in **single quotes** `'...'` or **double quotes** 
`"..."` with the same result

Python strings cannot be changed — they are **immutable**.

The built-in function `len()` returns the length of a string

If you don’t want characters prefaced by `\` to be interpreted as 
**special characters**,we can use **raw strings** by adding an `r` 
before the first quote.

_Example:_ Raw string
```Python
	print(r'C:\some\name')
	C:\some\name
```

String literals can span **multiple lines**. One way is using triple-quotes: 
`"""..."""` or `'''...'''`.

_Example:_ Multiline string
```Python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

Strings can be **concatenated** with the `+` operator, and **repeated** 
with `*`

_Example:_
```Python
assert 3 * 'un' + 'ium' == 'unununium'
```

Two or more string literals next to each other are automatically concatenated.

Strings can be **indexed**, with the first character having index 0.
There is no separate character type - **a character is simply a string of size one**.

_Example:_
```Python
word = 'Python'
assert "P" == word[0]
assert "n" == word[5]
```

**Indices may also be negative numbers**, to start counting from the right.

_Example:_
```Python
word = "Python"
assert "n" == word[-1]
assert "P" == word[-6]
```

Attempting to use an index that is too large will result in an error.

In addition to indexing, **slicing** is also supported.
While indexing is used to obtain individual characters, slicing allows you to
obtain substring.

_Example:_
```Python
word = "Python"
assert "Py" == word[0:2]    # [0,2)
assert "tho" == word[2:5]   # [2,5)
```

The built-in function **len()** returns the length of a string:

_Example:_
```Python
assert len("supercalifragilisticexpialidocious") == 34
```

We can **convert strings into numbers** using the `int()` and `float()` functions.

_Example:_
```Python
assert 7 == int("7")
assert 3.14 == float("3.14")
```

Also, **numbers can be converted into strings** using the `str()` function.

_Example:_
```Python
assert "13" == str(13)
assert "3.14" == str(3.14)
```

A format string is a way to insert variables into strings in Python dynamically. 

**Formatted String Literals** a.k.a. **f-strings** are the most modern and 
recommended way to format strings in Python.

_Example:_ f-string
```Python
name = "David"
age = 28
print(f"My name is {name} and I am {age} years old.")
```

_Example:_ Expressions inside f-strings
```Python
a = 10
b = 5
print(f"The sum of {a} and {b} is {a + b}.")
```

_Example:_ Formatting numbers
```Python
pi = 3.1415926535
print(f"Pi rounded to 2 decimal places: {pi:.2f}")    
```

_Example:_ Adding padding and alignment
```Python
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")
# Output: |Left      |  Center  |     Right|
```


## Lists

A list can be written as a **sequence of comma-separated values (items) 
between square brackets**.

Lists might contain items of different types, but usually the items all 
have the same type.

_Example:_ List of numbers
```Python
squares = [1, 4, 9, 16, 25]
assert squares == [1, 4, 9, 16, 25]
```

Like strings, **lists can be indexed and sliced**:
_Example:_ Indexing a list
```Python
squares = [1, 4, 9, 16, 25]
assert 1 == squares[0]
assert 25 == squares[-1]
```

_Example:_ Slicing a list
```Python
squares = [1, 4, 9, 16, 25]
assert [4,9] == squares[1:3]
assert [1,4,9] == squares[:3]
assert [16, 25] == squares[3:]
```

Lists also support operations like **concatenation**:

_Example:_ Concatenation of lists
```Python
assert [1, 2, 3, 4, 5, 6, 7] == [1, 2, 3, 4] + [5, 6, 7]
```

Unlike strings, **lists are a mutable** type, i.e. it is possible 
to change their content:

_Example:_ Change elements of a list
```Python
squares[0] = 99
assert [99, 4, 9, 16, 25] == squares
```

We can also **add new items at the end of the list**, by using 
the `append()` method:

_Example:_ Extend a list
```Python
squares = [1, 4, 9, 16, 25]
squares.append(6**2)
assert [1, 4, 9, 16, 25, 36] == squares
```

The built-in function `len()` can also be used to get the 
**size of a list**:

_Example:_ Size a list
```Python
squares = [1, 4, 9, 16, 25]
assert len(squares) == 5
```

It is possible to **nest lists** (create lists containing 
other lists):

_Example:_ Lists in a list
```Python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
assert [['a', 'b', 'c'], [1, 2, 3]] == x
```

## Tuples

A tuple consists of a number of values separated by commas.
Tuples are **immutable**, and usually contain a heterogeneous 
sequence of elements.

_Example:_ Tuples can be defined **with or without surrounding parentheses**.
```Python
numbers = 1, 2, 3, 4, 5
assert numbers == (1, 2, 3, 4, 5)
```

Note that the **== operator** compares element by element.


A special problem is the construction of tuples containing 
0 or 1 items: the syntax has some extra quirks to accommodate 
these.
**Empty tuples** are constructed by an empty pair of parentheses;
a **tuple with one item** is constructed by following a value with 
a comma (it is not sufficient to enclose a single value in parentheses).

_Example:_ **Empty tuples** are constructed by an empty pair of parentheses 
```Python
numbers = ()
assert numbers == ()
assert not numbers
```

Note that `not numbers` can be used to check if a tuple is empty.


_Example:_ Tuple with one item is constructed by a value with a comma
```Python
singleton = 'hello',    # Note trailing comma!!
assert singleton == ('hello',)
```

_Example:_ Tuple unpacking
```Python
t = 1, 4, 9
x, y, z = t
assert 1 == x
assert 4 == y
assert 9 == z
```

_Example:_ Concatenation
```Python
assert (1, 2, 3, 4, 5, 6, 7) == (1, 2, 3, 4) + (5, 6, 7)
```

_Example:_ Indexing
```Python
squares = (1, 4, 9, 16, 25)
assert 1 == squares[0]
assert 25 == squares[-1]
```

_Example:_ Slicing
```Python
squares = (1, 4, 9, 16, 25)
assert (4,9) == squares[1:3]
assert (1,4,9) == squares[:3]
assert (16, 25) == squares[3:] 
```

_Example:_ Length of a tuple
```Python
squares = (1, 4, 9, 16, 25)
assert len(squares) == 5
```

_Example:_ Nested tuples
```Python
a = ('a', 'b', 'c')
n = (1, 2, 3)
nested = (a, n)
assert (('a', 'b', 'c'), (1, 2, 3)) == nested
```

# Sets 

 A set is an **unordered collection with no duplicate elements**. 
 
 Basic uses include membership testing and eliminating duplicate entries. 
 Set objects also support mathematical operations like union, intersection, 
 difference, and symmetric difference.

_Example:_ Eliminate duplicates
```Python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
assert basket == {'apple', 'orange', 'pear', 'banana'}
```

_Example:_ To create an empty set we can use set(), not {};
```Python
empty_set = {}
assert not empty_set
```

_Example:_ Fast membership testing 
```Python
assert 'orange' in basket
assert 'crabgrass' not in basket```


_Example:_ Iterate over a set
```Python
for fruit in ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']:
    assert fruit in basket
```



## Dictionaries

Dictionaries are sometimes found in other languages as “associative memories” 
or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, 
**dictionaries are indexed by keys**, which can be any immutable type; strings 
and numbers can always be keys. 

It is best to think of a dictionary as a **set of key:value pairs**, with the 
requirement that the keys are unique (within one dictionary). 

A pair of braces creates an **empty dictionary**: `{}`. 

Placing a comma-separated list of `key:value` pairs within the braces adds initial 
`key:value` pairs to the dictionary; this is also the way dictionaries are written 
on output.

_Examples:_ Creating a dictionary
```Python
person = {
    "name": "Homer",
    "age": 25,
    "city": "New York"
}
assert person == {'name': 'Homer', 'age': 25, 'city': 'New York'}
```


_Examples:_ Accessing elements
```Python
assert "Homer" == person["name"]
assert 25 == person["age"]
assert "New York" == person["city"]
```

_Examples:_ Adding elements
```Python
person["email"] = "homer@powerplant.com"
assert "homer@powerplant.com" == person["email"]
```

_Examples:_ Removing elements
```Python
del person["email"]
assert "email" not in person
```

_Examples:_ Length of a dictionary
```Python
assert 3 == len(person)
```

_Examples:_ Retrieve keys, values, and items
```Python
assert sorted(person.keys()) == ['age', 'city', 'name']
print(person.values())
assert sorted(person.items()) == [('age', 25), ('city', 'New York'), ('name', 'Homer')]
```

_Examples:_ Iterate over a dictionary
```Python
for key, value in person.items():
    print(key, value)
```

_Examples:_ Loop over two or more sequences at the same time
```Python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
```


## Tutorials
* [YouTube (Corey Schafer): Integers and Floats - Working with Numeric Data](https://youtu.be/khKv-8q7YmY)
* [YouTube (Corey Schafer): Strings - Working with Textual Data](https://youtu.be/k9TUPpGqYTo)
* [YouTube (Corey Schafer): F-Strings - How to Use Them and Advanced String Formatting](https://youtu.be/nghuHvKLhJA)

* [YouTube (Corey Schafer): Lists, Tuples, and Sets](https://youtu.be/W8KRzm-HUcc)
* [YouTube (Corey Schafer): Dictionaries - Working with Key-Value Pairs](https://youtu.be/daefaLgNkw0)
* [YouTube (Corey Schafer): String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates](https://youtu.be/vTX3IwquFkc)


## References
* [Python Language Reference: Data Model](https://docs.python.org/3/reference/datamodel.html)

* [Python Tutorial: Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
* [Python Tutorial: Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
* [Python Tutorial: List](https://docs.python.org/3/tutorial/introduction.html#lists)

* [Python Tutorial: Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
* [Python Tutorial: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

*Egon Teiniker, 2020-2025, GPL v3.0*
