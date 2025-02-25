# Types in Python

Objects are Python’s abstraction for data. All data in a Python program is
represented by objects or by relations between objects.

Every object has an **identity**, a type and a value.
An object’s identity never changes once it has been created; you may think of
it as the object’s address in memory. The ‘is’ operator compares the identity
of two objects; the id() function returns an integer representing its identity.

An object’s **type** determines the operations that the object supports and also
defines the possible values for objects of that type. The type() function returns
an object’s type. An object’s type is also unchangeable.

The value of some objects can change. Objects whose value can change are said to
be mutable; objects whose value is unchangeable once they are created are called immutable.
An object’s mutability is determined by its type; for instance, numbers, strings and tuples
are immutable, while dictionaries and lists are mutable.
If an immutable container (like a tuple) contains a reference to a mutable object,
its value changes if that mutable object is changed.

Objects are never explicitly destroyed; however, when they become unreachable they
may be garbage-collected.


## Numbers
The **integer numbers** (e.g. 2, 4, 20) have type `int`, the ones with a fractional part
(e.g. 5.0, 1.6) have type **float**.
Division `/` always returns a float.
To do floor division and get an integer result you can use the `//` operator;
to calculate the remainder you can use `%` It is possible to use the `**` operator to calculate powers.

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
They can be enclosed in **single quotes** ('...') or **double quotes** ("...") with the same result

Python strings cannot be changed — they are **immutable**.

The built-in function `len()` returns the length of a string

If you don’t want characters prefaced by `\` to be interpreted as **special characters**,
we can use **raw strings** by adding an `r` before the first quote.
_Example:_ Raw string
```Python
	print(r'C:\some\name')
	C:\some\name
```

String literals can span **multiple lines**. One way is using triple-quotes: `"""..."""`
or `'''...'''`.
_Example:_ Multiline string
```Python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

Strings can be **concatenated** with the `+` operator, and **repeated** with `*`
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

Indices may also be negative numbers, to start counting from the right.
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
```Python
assert 7 == int("7")
assert 3.14 == float("3.14")
```

Also, **numbers can be converted into strings** using the `str()` function.
```Python
assert "13" == str(13)
assert "3.14" == str(3.14)
```

## Lists

A list can be written as a **sequence of comma-separated values (items) between square brackets**.
Lists might contain items of different types, but usually the items all have the same type.
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
_Example:_ Concatination of lists
```Python
assert [1, 2, 3, 4, 5, 6, 7] == [1, 2, 3, 4] + [5, 6, 7]
```

Unlike strings, **lists are a mutable** type, i.e. it is possible to change their content:
_Example:_ Change elements of a list
```Python
squares[0] = 99
assert [99, 4, 9, 16, 25] == squares
```

We can also **add new items at the end of the list**, by using the `append()` method:
_Example:_ Extend a list
```Python
squares = [1, 4, 9, 16, 25]
squares.append(6**2)
assert [1, 4, 9, 16, 25, 36] == squares
```

The built-in function `len()` can also be used to get the **size of a list**:
_Example:_ Size a list
```Python
squares = [1, 4, 9, 16, 25]
assert len(squares) == 5
```

It is possible to **nest lists** (create lists containing other lists):
_Example:_ Lists in a list
```Python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
assert [['a', 'b', 'c'], [1, 2, 3]] == x
```

## Tuples

A tuple consists of a number of values separated by commas.
Tuples are **immutable**, and usually contain a heterogeneous sequence of elements.


A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these.
**Empty tuples** are constructed by an empty pair of parentheses;
a **tuple with one item** is constructed by following a value with a comma
(it is not sufficient to enclose a single value in parentheses).



## References
* [Python Language Reference: Data Model](https://docs.python.org/3/reference/datamodel.html)

* [Python Tutorial: Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
* [Python Tutorial: Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
* [Python Tutorial: List](https://docs.python.org/3/tutorial/introduction.html#lists)

* [Python Tutorial: Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)


 *Egon Teiniker, 2020-2023, GPL v3.0*
