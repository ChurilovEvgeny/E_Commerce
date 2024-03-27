class Product:
    def __init__(self, name: str, description: str, price: float, count: int):
        self.name = name
        self.description = description
        self.__price = price
        self.count = count

    @property
    def price(self):
        return self.__price

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
    def make(cls, name: str, description: str, price: float, count: int, category=None):
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
