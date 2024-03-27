import pytest

from src.product import Product

from src.category import Category


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


def test_category_init(get_books, get_medicines):
    assert Category.categories_count == 0
    assert Category.products_unique_count == 0

    books_category = Category("Книги", "Литература", get_books)
    assert Category.categories_count == 1
    assert Category.products_unique_count == 3
    assert books_category.name == "Книги"
    assert books_category.description == "Литература"
    assert books_category.products == ('Чехов. Остров Сахалин, 450.5 руб. Остаток: 3 шт.\n'
                                       'Кошко. Уголовный мир царской России, 120.0 руб. Остаток: 10 шт.\n'
                                       'Тургенев. Отцы и дети, 100.0 руб. Остаток: 25 шт.')

    medicines_category = Category("Медикаменты", "Разные медикаменты", get_medicines)
    assert Category.categories_count == 2
    assert Category.products_unique_count == 5
    assert medicines_category.name == "Медикаменты"
    assert medicines_category.description == "Разные медикаменты"
    assert medicines_category.products == ('Аспирин, 20 руб. Остаток: 300 шт.\n'
                                           'Ибупрофен, 40 руб. Остаток: 150 шт.')


def test_add_product(get_medicines, get_additional_medicines):
    medicines_category = Category("Медикаменты", "Разные медикаменты", get_medicines)
    assert Category.categories_count == 3 # НЕ ЗАБЫВАЕМ, что это ГЛОБАЛЬНЫЕ счетчики
    assert Category.products_unique_count == 7

    medicines_category.add_product(get_additional_medicines)
    assert Category.categories_count == 3
    assert Category.products_unique_count == 8
    assert medicines_category.description == "Разные медикаменты"
    assert medicines_category.products == ('Аспирин, 20 руб. Остаток: 300 шт.\n'
                                           'Ибупрофен, 40 руб. Остаток: 150 шт.\n'
                                           'Спирт, 99 руб. Остаток: 400 шт.')
