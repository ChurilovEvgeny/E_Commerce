import json
from json import JSONDecodeError

from src.product import Product
from src.category import Category


def load_categories(filepath: str) -> list[Category] | list:
    """
    Функция загружает json-файл и возвращает преобразованный список Category
    :param filepath: путь к json-файлу
    :return: список Category или пустой список []
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [Category(c["name"], c["description"],
                             [Product(p["name"], p["description"], p["price"], p["quantity"]) for p in c["products"]])
                    for c in json.load(f)]

    except (FileNotFoundError, JSONDecodeError) as e:
        return []
