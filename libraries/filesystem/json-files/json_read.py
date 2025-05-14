import json

with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    print(type(data))
    print(data)

# Parsing JSON data: {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}

person = data['person']
print(person)   # {'name': 'John', 'age': 30, 'city': 'Graz'}

name = person['name']
print(name)     # John

age = person['age']
print(age)      # 30

city = person['city']
print(city)     # Graz
