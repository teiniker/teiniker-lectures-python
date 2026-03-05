class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if len(value) == 0:
            raise ValueError(f"Invalid description: '{value}'!'")
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(f"Invalid price: {value}!")
        self._price = value

    def __str__(self):
        return f"{self.description} ({self.price})"

    def __repr__(self):
        return f"Product(description={self.description!r}, price={self.price})"
