# Loops

## for Loop

The for loop in Python is used to iterate over a sequence 
(such as a list, tuple, dictionary, string, or range) and 
execute a block of code multiple times.

```python
for variable in sequence:
    # Code to execute
```

* `variable` is a temporary placeholder that takes each 
    value from the sequence (list, tuple, range, etc.).
* `sequence` is the collection of elements that the loop 
    will iterate through.
* The indented block of code executes for each iteration.


_Example:_  Loop from 0 to 9

```python
for i in range(10):
    print(i)
```


_Example:_ Loop from 5 to 14

```python
for i in range(5, 15):
    print(i)
```


_Example:_ Loop from 0 to 90 with step 10

```python
for i in range(0, 100, 10):
    print(i)

```


_Example:_ Breaking out of a loop

```python
for num in range(10):
    if num == 5:
        break  # Stops the loop when num is 5
    print(num)
```


_Example:_ Skipping an iteration

```python
for num in range(5):
    if num == 2:
        continue  # Skips when num is 2
    print(num)
```


_Example:_ Iterate over the elements of a list

```python
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
for value in values:
    print(value)
```


_Example:_ Iterate over the keys and values of a dictionary

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)
```

## Tutorials
* [YouTube (Corey Schafer): Loops and Iterations - For/While Loops](https://youtu.be/6iF8Xb7Z3wQ)
* [YouTube: Loop like a native: while, for, iterators, generators](https://youtu.be/EnSu9hHGq5o)


## References
* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)

*Egon Teiniker, 2020-2026, GPL v3.0*