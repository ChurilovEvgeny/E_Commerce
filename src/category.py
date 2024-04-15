from src.console_log import MixinConsoleLog
from src.product import Product


class Category(MixinConsoleLog):
    categories_count = 0
    products_unique_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = []
        for pr in products:
            self.add_product(pr)

        Category.categories_count += 1

        if type(self) is Category:
            print(MixinConsoleLog.__repr__(self))

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        return sum([i.count for i in self.__products])

    def __iter__(self):
        return iter(self.__products)

    @property
    def products(self):
        return "\n".join(map(str, self.__products))

    def add_product(self, product: Product):
        """
        Добавляет новый продукт в категорию
        :param product: добавляемый продукт
        :return: None
        """
        if not isinstance(product, Product):
            raise TypeError("Передаваемый объект обязан быть Product или его наследник")

        if product.count == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.__products.append(product)
        Category.products_unique_count += 1

    def get_product_properties(self, name: str):
        """
        Возвращает цену и количество продукта. Если такого продукта нет, то (0, 0)
        :param name: наименование продукта
        :return: цена и количество продукта
        """
        for p in self.__products:
            if p.name.lower() == name.lower():
                return p.price, p.count
        return 0, 0

    @classmethod
    def reset_global_counters(cls):
        """
        Сброс счетчиков количества экземпляров категорий и количества экземпляров продуктов
        НЕОБХОДИМО для предсказуемой проверки тестов
        :return: None
        """
        cls.categories_count = 0
        cls.products_unique_count = 0
