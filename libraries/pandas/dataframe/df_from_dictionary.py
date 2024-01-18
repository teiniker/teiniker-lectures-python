import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)

# Accessing a row by integer location
row_0 = df.iloc[0]
print(row_0)

# Accessing an element by integer location
element = df.iloc[0, 1]  # First row, second column
print(element)
