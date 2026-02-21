# Classes

In **object-oriented programming** we write **classes** that represent 
real-world things and situations, and we create **objects** based on 
these classes.

When we write a class, we define the general behavior that a whole 
category of objects can have. 
When we create individual objects from the class, each object is automatically 
equipped with the general behavior; we can then give each object whatever 
unique properties we desire.

Making an object from a class is called **instantiation**, and we work 
with instances of a class (a.k.a. objects).

## Defining a Class
Class names should be written in CamelCaps.
Instance and module names should be written in lowercase with underscores 
between words. 
Every class should have a docstring immediately following the class definition.

_Example_: Resistor
```Python
class Resistor():
    """Simulates a resistor with a given tolerance."""

    def __init__(self, value, tolerance=2):
        self._value = value              
        self._tolerance = tolerance       

    def get_value(self):
        return self._value

    def get_tolerance(self):
        return self._tolerance
``` 

### The `__init__()` Method 
This method Python runs automatically whenever we create a **new instance 
of a class**.

The **self parameter** is required in the method definition, and it must 
come first before the other parameters.
Every method call associated with a class automatically passes self, which 
is a reference to the instance itself; it gives the individual instance 
access to the attributes and methods in the class.


### Attributes
Attributes created in `__init__()` are called **instance attributes**. 
An instance attribute’s value is specific to a particular instance of 
the class.

On the other hand, **class attributes** are attributes that have the 
same value for all class instances. 
We can define a class attribute by assigning a value to a variable 
name outside of `__init__()`.

**Private attributes** that cannot be accessed except from inside an 
object don't exist in Python.
There is a convention that is followed by most Python code: 
a **name prefixed with two underscores** (e.g. `__value`) 
should be treated as a non-public part of the API (whether it is a 
function, a method or a data member).

Every attribute in a class needs an initial value, even if that value 
is 0 or an empty string. 
In some cases, such as when setting a **default value**, it makes 
sense to specify this initial value in the body of the `__init__()` 
method.

We can **change an attribute’s value** in three ways: 
* We can change the value directly through an instance
* Set the value through a method
* Increment the value (add a certain amount to it) through a method.


### Methods
Instance methods are functions that are defined inside a class and 
can only be called from an instance of that class. 
An instance method’s first parameter is always `self`.


### Access Modifiers in Python 

Object-oriented languages, like C++ and Java, use various keywords 
to control and restrict the resource usage of a class.

This is where keywords like `public`, `private` and `protected` come 
into the picture. However, Python has a different way of providing 
the functionality of these access modifiers.

* **Public** members of a class are available to everyone. 
   So they can be accessed from outside the class and also by other 
   classes too.

   All members of a class are by **default** public in Python. 
   These members can be accessed outside of the class, and their 
   values can be modified too.

* **Protected** members of a class can be accessed by other members 
    within the class and are also available to their subclasses.
    No other entity can access these members. 

    Python has a unique convention to make a member protected: 
    Add a prefix `_` (single underscore). This prevents its usage by 
    outside entities unless it is a subclass.

    The attribute defined in the above program is accessible outside 
    the class scope. It can also be modified as well.

* **Private** members of a class are only accessible within the class. 
    In Python, a private member can be defined by using a prefix 
    `__` (double underscore).

    Python performs name mangling on private attributes. 
    Every member with a double underscore will be changed to 
    `_object._class__variable`.

Double underscores are not very common in practice.
If we need to define attributes as private, we use a single underscore, 
and respect the Python convention that it is a private attribute.


### Properties
Properties are used when we need to define **access control** to some 
attributes in an object.

In other programming languages like Java, we create access methods 
(getters and setters) but in Python we use properties instead.

```Python
    @property
    def tolerance(self):
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        if tolerance < 0:
            raise ValueError('Invalid tolerance!')
        self._tolerance = tolerance
```

The `@property` method will return the value held by a private attribute.

The `@<property-name>.setter` method takes a value and validates it before 
the value will be stored in a private attribute.

```Python
r1 = Resistor(100,1)
assert 100 == r1.value
assert 1 == r1.tolerance
```
Note that the usage of properties is **transparent to the code outside a class**.


## Making an Class Instance

When Python reads the following line, it calls the `__init__()` method:

_Example_: 
```Python
r1 = Resistor(2700,2)
r2 = Resistor(2700,2)
``` 

The `__init__()` method has no explicit return statement, but Python 
automatically returns an instance.
We can create as many instances from a class as we need.


## Accessing Attributes and Calling Methods

To **access the attribute** of an instance, we use the **dot notation**.

To **call a method**, give the name of the instance and the method we 
want to call, separated by a dot.

_Example_: 
```Python
r1.value = 1000
r2.add(r1)
``` 


## Magic (Dunder) Methods

Python does all operations (`+`, `*`, `==`, etc.) using magic methods. 
These special methods have a naming convention, where the name 
starts with two underscores, followed by an identifier and ends with 
another pair of underscores.

Essentially, each built-in function or operator has a special method 
corresponding to it. 
For example, there’s `__eq__()`, corresponding to `==`, and `__add__()`, 
corresponding to the `+` operator.

By default, most of the built-ins and operators will not work with 
objects of our classes. 
We must add the corresponding special methods in our class definition 
to make our object compatible with built-ins and operators.

Due to the naming convention used for these methods, they are also 
called **dunder methods** which is a shorthand for **d**ouble **under**score 
methods. Sometimes they’re also referred to as special methods or 
**magic methods**. 


### The `__repr__()` Method
Python `__repr__()` function returns the object representation in 
string format. 
This method is called when `repr()` function is invoked on the object. 
If possible, the string returned should be **a valid Python expression 
that can be used to reconstruct the object again**.

_Example_: 
```Python
    def __repr__(self):
        return 'Resistor({}, {})'.format(self.get_value(), self.get_tolerance())
``` 


### The `__str__()` Method
This method returns the **string representation of the object**. 
This method is called when `print()` or `str()` function is invoked 
on an object.

This method must return the String object. 
If we don’t implement `__str__()` function for a class, then built-in 
object implementation is used that actually calls `__repr__()` function.

We should always use `str()` function, which will call the underlying 
`__str__()` function. 
It’s not a good idea to use the `__str__()` function directly.

_Example_: 
```Python
    def __str__(self):
        return 'Resistor: value={}, tolerance={}'.format(self.get_value(), self.get_tolerance())    
``` 


### The `__eq__()` Method
There are various ways using which the objects of any type in Python can 
be compared. 
The `==` operator compares the value or equality of two objects, whereas 
the Python `is` operator checks whether two variables point to the same 
object in memory.

Python automatically calls the `__eq__()` method of a class when you use 
the `==` operator to compare the instances of the class. 
By default, Python uses the `is` operator if you don’t provide a specific 
implementation for the `__eq__()` method.

_Example_: 
```Python
    def __eq__(self, other):
        if self._value == other._value and self._tolerance == other._tolerance:
            return True
        else:
            return False
``` 

### The `__add__()` Method
The special method corresponding to the `+` operator is the `__add__()` method. 
Adding a custom definition of `__add__()` changes the behavior of the operator. 
It is recommended that `__add__()` returns a new instance of the class instead 
of modifying the calling instance itself. 

_Example_: 
```Python
    def __add__(self, other):
        return Resistor(self._value + other._value)
``` 


## Inheritance
When one class inherits from another, it automatically **takes on all the 
attributes and methods of the first class**. The original class is called 
the **parent class**, and the new class is the **child class**.

The child class inherits every attribute and method from its parent class 
but is also free to define new attributes and methods of its own.

When we create a child class, the parent class must be part of the current 
file and must appear before the child class in the file. 
The name of the parent class must be included in parentheses in the definition 
of the child class.

The `super()` function is a special function that helps Python make 
connections between the parent and child class. The name super comes 
from a convention of calling the parent class a **superclass** and 
the child class a **subclass**.

The `__init__()` method for a child class needs help from its parent 
class, so it calls `super().__init__()` to initialize the attributes 
of the parent class.

Once we have a child class that inherits from a parent class, we can 
**add any new attributes and methods** necessary to differentiate the 
child class from the parent class.

We can **override** any method from the parent class that doesn’t 
fit what we’re trying to model with the child class. 
To do this, we define a method in the child class with the same name 
as the method you want to override in the parent class.
Python will disregard the parent class method and only pay attention 
to the method you define in the child class.


## Tutorials
* [YouTube (Corey Schafer): Classes and Instances](https://youtu.be/ZDa-Z5JzLYM)
* [YouTube (Corey Schafer): Property Decorators - Getters, Setters, and Deleters](https://youtu.be/jCzT9XFZ5bw)
* [YouTube (Corey Schafer): Special (Magic/Dunder) Methods](https://youtu.be/3ohzBxoFHAY)
* [YouTube (Corey Schafer): Class Variables](https://youtu.be/BJ-VvGyQxho)
* [YouTube (Corey Schafer): Classmethods and Staticmethods](https://youtu.be/rq8cL2XMM5M)
 

## References
* Eric Matthes. Python Crash Course. No Starch Press, 2016. 
    * Chapter 9: Classes

* Mariano Anaya. Clean Code in Python. Packt Publishing, 2018. 
    * Chapter 2: Pythonic Code

* [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

* [Public, Private, and Protected — Access Modifiers in Python](https://betterprogramming.pub/public-private-and-protected-access-modifiers-in-python-9024f4c1dd4)

* [Operator and Function Overloading in Custom Python Classes](https://realpython.com/operator-function-overloading/)
* [Python __str__() and __repr__() functions](https://www.journaldev.com/22460/python-str-repr-functions)
* [Python __eq__](https://www.pythontutorial.net/python-oop/python-__eq__)


*Egon Teiniker, 2020-2026, GPL v3.0*
