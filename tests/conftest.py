import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def get_books():
    return [Product("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3),
            Product("Кошко. Уголовный мир царской России", "Мемуары", 120.0, 10),
            Product("Тургенев. Отцы и дети", "Роман", 100.0, 25)]


@pytest.fixture
def get_medicines():
    return [Product("Аспирин", "От всего", 20, 300),
            Product("Ибупрофен", "От боли", 40, 150), ]


@pytest.fixture
def get_additional_medicines():
    return Product("Спирт", "Для всего", 99, 400)


@pytest.fixture
def get_book_category_without_products():
    return Category("Книги", "Литература", [])


@pytest.fixture
def get_book_category_with_products(get_books):
    return Category("Книги", "Литература", get_books)
