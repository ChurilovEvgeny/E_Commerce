from abc import ABC, abstractmethod


class Good(ABC):

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @price.deleter
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def total_price(self):
        pass
