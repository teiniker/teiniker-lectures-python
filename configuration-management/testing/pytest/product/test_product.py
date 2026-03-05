import pytest
from product import Product

class TestProduct:
    def setup_method(self):
        self.product = Product("dvd", 1799)

    def teardown_method(self):
        self.product = None

    def test_product(self):
        assert self.product.description == "dvd"
        assert self.product.price == 1799

    def test_product_invalid_price(self):
        with pytest.raises(ValueError):
            self.product.price = -1790

    def test_product_invalid_description(self):
        with pytest.raises(ValueError):
            self.product.description = ""

    def test_product_str(self):
        assert str(self.product) == "dvd (1799)"

    def test_product_repr(self):
        assert repr(self.product) == "Product(description='dvd', price=1799)"
