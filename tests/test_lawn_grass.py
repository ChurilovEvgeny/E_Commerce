from src.lawn_grass import LawnGrass


def test_lawn_grass_init():
    p = LawnGrass("Трава", "Трава у дома", 1000, 1, "Родина", "10", "Red")
    assert p.name == "Трава"
    assert p.description == "Трава у дома"
    assert p.price == 1000
    assert p.count == 1
    assert p.manufacturer_country == "Родина"
    assert p.germination_period == "10"
    assert p.color == "Red"