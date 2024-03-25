import pytest

from src.utils import load_categories

def test_load_categories():
    c = load_categories("data/products.json")
    assert len(c) == 2

    c = load_categories("data/empty.json")
    assert c == []

    c = load_categories("data/empty_file.json.json")
    assert c == []

    c = load_categories("file_not_exist.json")
    assert c == []