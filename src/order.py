from src.console_log import MixinConsoleLog
from src.product import Product


class Order(MixinConsoleLog):
    def __init__(self, product: Product, product_count):
        self.product = product
        self.product_count = product_count
        if type(self) is Order:
            MixinConsoleLog.__init__(self)

    @property
    def total_price(self):
        return self.product.price * self.product_count

    def __repr__(self):
        return f"{self.__class__.__name__}({", ".join(map(str, self.__dict__.values()))})"

