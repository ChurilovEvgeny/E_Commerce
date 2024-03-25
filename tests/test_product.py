from src.product import Product


def test_product_init():
    p = Product("Чехов. Остров Сахалин", "Книга о путешествии А.П. Чехова на остров Сахалин", 450.5, 3)
    assert p.name == "Чехов. Остров Сахалин"
    assert p.description == "Книга о путешествии А.П. Чехова на остров Сахалин"
    assert p.price == 450.5
    assert p.count == 3
