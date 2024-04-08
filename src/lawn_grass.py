from src.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, count: int, manufacturer_country: str,
                 germination_period: str, color: str):
        super().__init__(name, description, price, count)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
