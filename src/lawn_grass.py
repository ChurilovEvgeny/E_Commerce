from src.console_log import MixinConsoleLog
from src.product import Product


class LawnGrass(Product, MixinConsoleLog):
    def __init__(self, name: str, description: str, price: float, count: int, manufacturer_country: str,
                 germination_period: str, color: str):
        super().__init__(name, description, price, count)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color

        if type(self) is LawnGrass:
            print(MixinConsoleLog.__repr__(self))
