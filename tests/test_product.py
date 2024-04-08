import pytest

from src.product import Product
from src.smartphone import Smartphone


def test_product_init():
    p = Product("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3)
    assert p.name == "Чехов. Остров Сахалин"
    assert p.description == "Книга о путешествии А.П. Чехова на остров Сахалин"
    assert p.price == 450.5
    assert p.count == 3


def test_dander():
    p1 = Product.make("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3)
    p2 = Product.make("Достоевский. Бесы", "Роман?", 1000, 2)
    assert p1 + p2 == 3351.5

    sm1 = Smartphone("T", "T", 100, 1, "1", "1", 50, "B")
    sm2 = Smartphone("T", "T", 150, 1, "1", "1", 50, "B")
    assert sm1 + sm2 == 250

    with pytest.raises(TypeError):
        p1 + sm1


def test_make(get_book_category_without_products, get_book_category_with_products):
    p = Product.make("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3)
    assert p.name == "Чехов. Остров Сахалин"
    assert p.description == "Книга о путешествии А.П. Чехова на остров Сахалин"
    assert p.price == 450.5
    assert p.count == 3

    p = Product.make("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3,
                     get_book_category_without_products)
    assert p.name == "Чехов. Остров Сахалин"
    assert p.description == "Книга о путешествии А.П. Чехова на остров Сахалин"
    assert p.price == 450.5
    assert p.count == 3

    p = Product.make("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 300, 3,
                     get_book_category_with_products)
    assert p.name == "Чехов. Остров Сахалин"
    assert p.description == "Книга о путешествии А.П. Чехова на остров Сахалин"
    assert p.price == 450.5
    assert p.count == 6


def test_price(monkeypatch):
    p = Product.make("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3)
    assert p.price == 450.5
    assert p.total_price == 1351.5

    p.price = -1
    assert p.price == 450.5

    p.price = 500
    assert p.price == 500

    monkeypatch.setattr('builtins.input', lambda _: "y")
    p.price = 400
    assert p.price == 400

    monkeypatch.setattr('builtins.input', lambda _: "n")
    p.price = 300
    assert p.price == 400

    del p.price
    assert p.price == 0
