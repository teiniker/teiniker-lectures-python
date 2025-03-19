import json

data = {
    "person": {
        "name": "John", 
        "age": 30, 
        "city": "Graz"
    }
}

with open('tmp.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)
