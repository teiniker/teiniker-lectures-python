import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

# Accessing element by index (can also be a string)
print(f"Element in index 2 = {series[2]}")
print(f"Elements where index > 2 = {series[series > 2]}")
