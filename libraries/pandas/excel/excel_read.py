import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name="data",  header=1, usecols="B:E")

print(df)
