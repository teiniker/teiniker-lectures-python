
class TextReader:
    def __init__(self, filename:str)->None:
        self.filename = filename
        self.file = None

    def __enter__(self):
        print(f"open file: {self.filename}")
        self.file = open(self.filename, 'r', encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        print(f"close file: {self.filename}")
        self.file.close()

# Verify Implementation

with TextReader("data.txt") as txt_file:
    data = txt_file.read()
    print(data)
