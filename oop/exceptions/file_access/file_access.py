import csv

class DataAccessError(Exception):
    pass

class DataAccessObject:
    def __init__(self, filename:str)->None:
        self.filename = filename

    def read_data(self)-> list[float]:
        file=None
        try:
            values:list[float] = []
            file = open(self.filename, 'r', encoding="utf-8")
            reader = csv.reader(file, delimiter=',')
            data = list(reader)
            for value in data:
                values.append(float(value[1]))
            return values
        except FileNotFoundError as ex:
            raise DataAccessError(f"File {self.filename} not found!") from ex
        finally:
            print("finally")
            if file:
                file.close()


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
