# Conditional Statements

Conditional statements in Python control the flow of execution by allowing 
the program to make decisions based on conditions. They enable the program 
to execute different blocks of code depending on whether a condition is 
`True` or `False`.

## if-else

The if-else statement in Python is a conditional control structure that 
allows the execution of different blocks of code based on a condition.

```Python
if condition:
    # Code executed if condition is True
else:
    # Code executed if condition is False
```

_Example:_ if-else statement

```Python   
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

The if statement checks if the variable age is greater than or equal 
to 18:
* If the condition is `True`, it executes the indented code under it:
   `print("You are an adult.")`
* If the condition in the if statement is `False` (meaning age is less 
    than 18), the code inside the else block runs:
   `print("You are a minor.")`


_Example:_ if-elif-else statement

```Python
num = 0

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

If the first condition `(num > 0)` is `False`, it checks if `num` is 
less than zero: `elif num < 0:` (**else-if statement**).


_Example:_ Using if-else with Logical Operators

```Python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club.")
else:
    print("You cannot enter.")
```

The condition uses the **and** operator, meaning both conditions must 
be `True` for the code inside if to execute.


_Example:_ Using if-else with in Operator

```Python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is available.")
else:
    print("Banana is not available.")
```

The **in** operator checks whether "banana" is present in the 
variable fruits.

It assumes that fruits is a collection, such as a `list`, 
`tuple`, or `set`.


## match-case

The match-case statement is **Python’s version of a switch-case**, 
introduced in Python 3.10. It allows pattern matching to simplify 
conditional statements.

```python
match variable:
    case pattern1:
        # Code to execute if variable matches pattern1
    case pattern2:
        # Code to execute if variable matches pattern2
    case _:
        # Default case if no match is found 
        # (similar to "default" in switch-case)
```

_Example:_ Convert a day's number into its name.

```Python
def get_day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(get_day_name(3))  # Output: Wednesday
print(get_day_name(10)) # Output: Invalid day            
```

* The function `def get_day_name(day)` takes an integer input 
    `day` representing a day of the week.

* The `match` statement checks the value of day against multiple    
    case conditions.

* Case-by-Case Checking:
    - If `day == 1`, it returns `"Monday"`.
    - If `day == 2`, it returns `"Tuesday"`, and so on.

* The underscore `_` acts as a **default case** (like else in an 
    `if-else` statement).

_Example:_ Matching Multiple Cases
    
```Python
def check_vowel(letter):
    match letter:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "It's a vowel."
        case _:
            return "It's a consonant."

print(check_vowel('e'))  # Output: It's a vowel.
print(check_vowel('b'))  # Output: It's a consonant.
```

Multiple Values in One Case `case 'a' | 'e' | 'i' | 'o' | 'u':`
The `|` (pipe symbol) acts as an **OR operator**.


_Example:_ Using case _ if for Conditional Matching

```Python
def number_type(num):
    match num:
        case x if x > 0:
            return "Positive number"
        case x if x < 0:
            return "Negative number"
        case 0:
            return "Zero"
        case _:
            return "Not a number"

print(number_type(10))   # Output: Positive number
print(number_type(-5))   # Output: Negative number
print(number_type(0))    # Output: Zero
```

* `case x if x > 0:` If num is greater than 0, it matches this case 

* `case x if x < 0:` If num is less than 0, it matches this case 

* `case 0:` If num is exactly 0, it matches this case.

* `case _:` If num does not match any of the above cases (e.g., if 
    it's `None`, a string, or another unexpected value)


_Example:_ Matching Data Structures (Tuples)

```Python
def process_coordinates(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"Point is on the X-axis at x={x}"
        case (0, y):
            return f"Point is on the Y-axis at y={y}"
        case (x, y):
            return f"Point is at ({x}, {y})"
        case _:
            return "Unknown format"

print(process_coordinates((0, 0)))  # Output: Origin
print(process_coordinates((5, 0)))  # Output: Point is on the X-axis at x=5
print(process_coordinates((3, 4)))  # Output: Point is at (3, 4)
```

Here, each case is defined by a **tuple pattern**.


## Tutorials
* [YouTube (Corey Schafer): Conditionals and Booleans - If, Else, and Elif Statements](https://youtu.be/DZwmZ8Usvnk)

## References
* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)


*Egon Teiniker, 2020-2026, GPL v3.0*