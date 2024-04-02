from src.category import Category


class ProductIterator:
    def __init__(self, category: Category):
        self.__iterator = iter(category)

    def __iter__(self):
        return self.__iterator

    def __next__(self):
        try:
            return next(self.__iterator)
        except StopIteration as e:
            raise e
