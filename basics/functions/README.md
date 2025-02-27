# Functions

The first organizational tool programmers use in Python is the function.
Functions enable us to **break large programs into smaller, simpler 
pieces with names** to represent their intent. They improve readability 
and make code more approachable. They allow for reuse and refactoring.

_Example:_
```Python
def max_value(a, b):
    """Calculate the maximum of two numbers"""
    if a > b:
        return a
    else:
        return b    
```

The variables `a` and `b` in the definition of `max_value()` are 
examples of **parameters**, a piece of information the function 
needs to do its job. 

An **argument** is a piece of information that is passed from a 
function call to a function. 
When we call the function, we place the value we want the function 
to work with in parentheses.


## Docstrings

Python documentation string or commonly known as docstring, is 
a **string literal**, and it is used in the class, module, 
function, or method definition. 

Docstrings are accessible from the doc attribute `__doc__` for 
any of the Python objects and also with the built-in `help()` 
function. 

An object's docstring is defined by including a string constant 
as the first statement in the object's definition.

Docstrings are similar in spirit to commenting, but they are 
enhanced, more logical, and useful version of commenting. 
Docstrings act as documentation for the class, module, and packages.

Docstrings are represented with closing and opening quotes while 
comments start with a `#` at the beginning.

There are a couple of ways of writing or using a Docstring:
* The **one-line docstrings** are the docstrings, which fits 
    all in one line. 
     We can use one of the quotes, i.e., triple single or 
     triple-double quotes, and opening quotes and closing quotes 
     need to be the same. 

* **Multi-line docstrings** also contains the same string 
    literals line as in one-line docstrings, but it is 
    followed by a single blank along with the descriptive text.


## Passing Arguments

Because a function definition can have multiple parameters, 
a function call may need multiple arguments. 
We can pass arguments to our functions in a number of ways. 

We can use **positional arguments**, which need to be in the 
same order the parameters were written; **keyword arguments**, 
where each argument consists of a variable name and a value.

* **Positional Arguments**: Python must match each argument 
    in the function call with a parameter in the function 
    definition. The simplest way to do this is **based on 
    the order of the arguments** provided. Values matched 
    up this way are called positional arguments.

    We can get unexpected results if we mix up the order of 
    the arguments in a function call when using positional 
    arguments.

    _Example_:
    ```Python
        user_to_string('homer', 'Drink4DuffBeers')
    ```

* **Keyword Arguments**. A keyword argument is a **name-value 
    pair** that you pass to a function. We directly associate 
    the name and the value within the argument, so when we pass 
    the argument to the function, there’s no confusion.
    Keyword arguments free us from having to worry about correctly 
    ordering your arguments in the function call, and they clarify 
    the role of each value in the function call.

    _Example_: 
    ```Python
        user_to_string(password='Drink4DuffBeers', username='homer')
    ```

When we pass a **list** to a function, the function gets direct 
access to the contents of the list (**call by reference**). 

When we pass a list to a function, the function can modify the list. 
Any changes made to the list inside the function’s body are permanent, 
allowing us to work efficiently even when we are dealing with large 
amounts of data.

Note that we can also **pass a copy** of a list into a function.
The slice notation `[:]` makes a copy of the list to send to the function.


## Default Values
When writing a function, we can define a default value for each parameter. 
If an argument for a parameter is provided in the function call, Python 
uses the argument value. If not, it uses the parameter’s default value.

Using default values can simplify our function calls and clarify the ways 
in which our functions are typically used.

Note that when we use default values, any parameter with a default value 
needs to be listed after all the parameters that don’t have default values.


## Return Values
The return statement takes a value from inside a function and sends it 
back to the line that called the function. 
Return values allow us to move much of your program’s work into functions, 
which can simplify the body of your program.

When we call a function that returns a value, we need to provide a variable 
where the return value can be stored. 
Later we use the return statement to pass the content of this variable 
back to the caller. 

A function can return any kind of value we need it to, including more 
complicated data structures like **lists** and **dictionaries**.


## References
* Eric Matthes. Python Crash Course. No Starch Press, 2016. Chapter 8: Functions

* [Docstrings in Python](https://www.datacamp.com/community/tutorials/docstrings-python)

*Egon Teiniker, 2020-2025, GPL v3.0*
