TEMPLATE = """
Hello {name}, 
I know you are {age} years old.
"""

def merge(name: str, age: int) -> str:
    return TEMPLATE.format(name=name, age=age)

def main():
    result = merge("Homer", 38)
    print(result)

if __name__ == "__main__":
    main()
