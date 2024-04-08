from src.smartphone import Smartphone


def test_smartphone_init():
    p = Smartphone("Honor", "Honor 30", 1000, 1, "high", "30", 6, "Red")
    assert p.name == "Honor"
    assert p.description == "Honor 30"
    assert p.price == 1000
    assert p.count == 1
    assert p.performance == "high"
    assert p.model == "30"
    assert p.build_in_mem == 6
    assert p.color == "Red"