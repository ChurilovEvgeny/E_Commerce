from src.product import Product


class Category:
    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = list(
            products)  # Копия, чтобы не было непредвиденного поведения с доступом по ссылке к исходному списку


