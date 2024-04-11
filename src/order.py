from src.console_log import MixinConsoleLog
from src.product import Product


class Order(MixinConsoleLog):
    def __init__(self, product: Product, product_count):
        self.product = product
        self.product_count = product_count
        if type(self) is Order:
            print(MixinConsoleLog.__repr__(self))

    @property
    def total_price(self):
        return self.product.price * self.product_count
