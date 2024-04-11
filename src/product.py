from typing import TYPE_CHECKING, Union

from src.console_log import MixinConsoleLog
from src.good import Good

if TYPE_CHECKING:
    from src.category import Category


class Product(Good, MixinConsoleLog):
    def __init__(self, name: str, description: str, price: float, count: int):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.count = count

        if type(self) is Product:
            print(MixinConsoleLog.__repr__(self))

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.count} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.total_price + other.total_price
        raise TypeError("Складывать товары разных типов запрещено!")

    @property
    def price(self):
        return self.__price

    @property
    def total_price(self):
        return self.count * self.price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("НОВАЯ цена некорректна <= 0!!!")
            return
        elif new_price < self.__price:
            while ((confirm_change := input("Новая цена меньше текущей! Подтвердите изменение (y/n)!").lower())
                   not in ("y", "n")):
                pass
            if confirm_change == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = 0

    @classmethod
    def make(cls, name: str, description: str, price: float, count: int, category: Union["Category", None] = None):
        """
        Метод фабрика для создания объекта Product.
        Если задан category, то в нем выполняется поиск объекта с таким-же именем.
        Если объект не найден, то создается новый объект Product исходя из параметров.
        Если объект найден, то выбирается максимальная цена, а количество складывается
        :param name: наименование продукта
        :param description: описание продукта
        :param price: цена продукта
        :param count: количество продукта
        :param category: объект Category, который в себе уже может содержать Product с именем name
        :return: новый объект Product
        """
        if category is None:
            return cls(name, description, price, count)
        else:
            price_cat, count_cat = category.get_product_properties(name)
            return cls(name, description, max(price, price_cat), count + count_cat)
