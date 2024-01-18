import json

with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    print(type(data))
    print(data)
