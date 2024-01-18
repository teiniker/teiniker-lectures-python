class Entity():
    """Base class for entity classed which provide an id."""
    def __init__(self, oid:int)->None:
        self.oid = oid

    def __eq__(self, other)->bool:
        return self.oid == other.oid


class Product(Entity):
    """Product class which supports a description and a price."""
    def __init__(self, oid:int, description:str, price:float)->None:
        super().__init__(oid)
        self.description = description
        self.price = price

    def __str__(self)->str:
        return f'Product: id={self.oid}, description="{self.description}", price={self.price}'


class OrderLine(Entity):
    def __init__(self, oid:int, quantity:int, product:Product)->None:
        super().__init__(oid)
        self.quantity = quantity
        self.product = product

    def __str__(self)->str:
        return f'OrderLine: id={self.oid}, quantity={self.quantity}, product={self.product}'


class Order(Entity):
    def __init__(self, oid:int, name:str)->None:
        super().__init__(oid)
        self.name = name
        self.lines:list[OrderLine] = []

    def add_line(self, line:OrderLine)->None:
        self.lines.append(line)

    def __str__(self)->str:
        lines_str = '; '.join([str(elem) for elem in self.lines])
        return f'Order: id={self.oid}, name={self.name}, lines=[{lines_str}]'


if __name__ == '__main__':

    # Verify implementations
    e1 = Entity(7)
    p1 = Product(3, "Pizza Frutti di Mare", 8.80)
    p2 = Product(3, "Pizza Frutti di Mare", 8.80)
    assert p1 == p2

    order = Order(1, "Pizza Order")
    line1 = OrderLine(2, 1, Product(3, "Pizza Frutti di Mare", 8.80))
    line2 = OrderLine(4, 1, Product(5, "Pizza Quattro Formaggi", 8.20))
    order.add_line(line1)
    order.add_line(line2)
    print(order)

    assert 1 == order.oid
    assert "Pizza Order" == order.name

    assert 2 == order.lines[0].oid
    assert 4 == order.lines[1].oid

    assert 3 == order.lines[0].product.oid
    assert 5 == order.lines[1].product.oid
