# For Loop Variants

# Loop from 0 to 9
for i in range(10):
    print(i)

# Loop from 5 to 14
for i in range(5, 15):
    print(i)

# Loop from 0 to 100 with step 10
for i in range(0, 101, 10):
    print(i)

# Iterate over the elements of a list
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
for value in values:
    print(value)

# Iterate over the keys and values of a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)
