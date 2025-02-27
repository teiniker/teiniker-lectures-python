# For Loop Variants

# Loop from 0 to 9
for i in range(10):
    print(i)


# Loop from 5 to 14
for i in range(5, 15):
    print(i)


# Loop from 0 to 90 with step 10
for i in range(0, 100, 10):
    print(i)


# Breaking out of a loop
for num in range(10):
    if num == 5:
        break  # Stops the loop when num is 5
    print(num)


# Skipping an iteration
for num in range(5):
    if num == 2:
        continue  # Skips when num is 2
    print(num)


# Iterate over the elements of a list
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
for value in values:
    print(value)


# Iterate over the keys and values of a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)
