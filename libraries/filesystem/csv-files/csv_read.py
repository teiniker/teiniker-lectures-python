import csv
import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

with open('data.csv', 'r', encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        print(f"line: {row[0]} data: {row[1]}")
