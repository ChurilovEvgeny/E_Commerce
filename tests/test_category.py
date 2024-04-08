import pytest

from src.category import Category


def test_category_init(get_books, get_medicines):
    Category.reset_global_counters()
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

    Category.reset_global_counters()
    assert Category.categories_count == 0
    assert Category.products_unique_count == 0


def test_dander(get_medicines):
    Category.reset_global_counters()
    medicines_category = Category("Медикаменты", "Разные медикаменты", get_medicines)

    assert len(medicines_category) == 450
    assert str(medicines_category) == "Медикаменты, количество продуктов: 450 шт."
    Category.reset_global_counters()


def test_add_product(get_medicines, get_additional_medicines):
    Category.reset_global_counters()
    medicines_category = Category("Медикаменты", "Разные медикаменты", get_medicines)
    assert Category.categories_count == 1  # НЕ ЗАБЫВАЕМ, что это ГЛОБАЛЬНЫЕ счетчики
    assert Category.products_unique_count == 2

    medicines_category.add_product(get_additional_medicines)
    assert Category.categories_count == 1
    assert Category.products_unique_count == 3
    assert medicines_category.description == "Разные медикаменты"
    assert medicines_category.products == ('Аспирин, 20 руб. Остаток: 300 шт.\n'
                                           'Ибупрофен, 40 руб. Остаток: 150 шт.\n'
                                           'Спирт, 99 руб. Остаток: 400 шт.')

    with pytest.raises(TypeError):
        medicines_category.add_product("STRING")


def test_get_products_properties(get_medicines):
    Category.reset_global_counters()
    medicines_category = Category("Медикаменты", "Разные медикаменты", get_medicines)
    price, count = medicines_category.get_product_properties("Аспирин")
    assert price == 20
    assert count == 300

    price, count = medicines_category.get_product_properties("НЕТ в категории")
    assert price == 0
    assert count == 0
