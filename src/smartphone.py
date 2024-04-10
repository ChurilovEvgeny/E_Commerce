from src.console_log import MixinConsoleLog
from src.product import Product


class Smartphone(Product, MixinConsoleLog):
    def __init__(self, name: str, description: str, price: float, count: int, performance: str, model: str,
                 build_in_mem: int, color: str):
        super().__init__(name, description, price, count)
        self.performance = performance
        self.model = model
        self.build_in_mem = build_in_mem
        self.color = color

        if type(self) is Smartphone:
            MixinConsoleLog.__init__(self)

    def __repr__(self):
        return Product.__repr__(self)