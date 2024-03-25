from src.product import Product


class Category:
    categories_count = 0
    products_unique_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = list(
            products)  # Копия, чтобы не было непредвиденного поведения с доступом по ссылке к исходному списку

        Category.categories_count += 1

        # Реализация подсчета количества уникальных продуктов несколько спорная, так как в теории
        # в одной категории могут быть несколько объектов Product с одинаковыми позициями
        # или же в разные категории могут попасть одинаковые Product
        # если такая возможность реальна, то, возможно, название Product надо хранить в set,
        # но пока так
        Category.products_unique_count += len(self.products)
