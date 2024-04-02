import pytest

from src.category import Category
from src.product_iterator import ProductIterator


def test_iterator(get_books):
    Category.reset_global_counters()

    books_category = Category("Книги", "Литература", get_books)
    p = ProductIterator(books_category)
    assert next(p).price == 450.5
    assert next(p).price == 120
    assert next(p).price == 100
    with pytest.raises(StopIteration):
        next(p)

    Category.reset_global_counters()
