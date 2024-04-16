from abc import ABC, abstractmethod

from src.e_exceptions import ZeroCountProductException
from src.product import Product


class AbsProductContainer(ABC):

    def add_product(self, product: Product):
        """
        Добавляет новый продукт
        :param product: добавляемый продукт
        :return: None
        """
        if not isinstance(product, Product):
            raise TypeError("Передаваемый объект обязан быть Product или его наследник")

        try:
            if product.count == 0:
                raise ZeroCountProductException()
        except ZeroCountProductException as e:
            print(e)
        else:
            self._add_product_in_object(product)
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @abstractmethod
    def _add_product_in_object(self, product: Product):
        pass
