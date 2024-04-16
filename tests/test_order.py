from src.order import Order


def test_get_total_price(get_additional_medicines):
    ord = Order(get_additional_medicines, 10)
    assert ord.total_price == 990