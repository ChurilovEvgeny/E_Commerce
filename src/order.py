from src.console_log import MixinConsoleLog
from src.e_exceptions import ZeroCountProductException
from src.product import Product
from src.abs_product_container import AbsProductContainer


class Order(AbsProductContainer, MixinConsoleLog):
    product: Product

    def __init__(self, product: Product, product_count):
        self.add_product(product)
        self.product_count = product_count
        if type(self) is Order:
            print(MixinConsoleLog.__repr__(self))

    @property
    def total_price(self):
        return self.product.price * self.product_count

    def _add_product_in_object(self, product: Product):
        self.product = product
