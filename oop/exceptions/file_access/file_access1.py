import csv

class DataAccessError(Exception):
    pass

class DataAccessObject:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=',')
                data = list(reader)
                values = [float(row[1]) for row in data]
                return values
        except FileNotFoundError as ex:
            raise DataAccessError(f"File {self.filename} not found!") from ex

# Context Manager (with Statement): The with open(...) as file: 
# construct is used to open the file. 
# This ensures that the file is automatically closed after the 
# block is executed, even if an exception occurs.


# Verify Implementation

dao = DataAccessObject('data.csv')
value_list = dao.read_data()
print(value_list)

try:
    dao = DataAccessObject('datx.csv')
    value_list = dao.read_data()
    print(value_list)
except DataAccessError as e:
    print(e)
