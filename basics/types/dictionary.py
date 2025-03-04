# Dictionary objects

# A dictionary is an unordered collection of key-value pairs.

# Create a dictionary
person = {
    "name": "Homer",
    "age": 25,
    "city": "New York"
}
assert person == {'name': 'Homer', 'age': 25, 'city': 'New York'}

# Accessing elements
assert "Homer" == person["name"]
assert 25 == person["age"]
assert "New York" == person["city"]

# Adding elements
person["email"] = "homer@powerplant.com"
assert "homer@powerplant.com" == person["email"]

# Removing elements
del person["email"]
assert "email" not in person

# Length of a dictionary
assert 3 == len(person)

# Dictionary methods
assert sorted(person.keys()) == ['age', 'city', 'name']
print(person.values())
assert sorted(person.items()) == [('age', 25), ('city', 'New York'), ('name', 'Homer')]

# Iterate over a dictionary
for key, value in person.items():
    print(key, value)

# Loop over two or more sequences at the same time
# The entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
