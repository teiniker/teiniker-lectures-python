import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# Read the contents of a text file
with open('data.txt', 'r', encoding="utf-8") as in_file:
    for line in in_file:
        print(f"> {line}", end='')
