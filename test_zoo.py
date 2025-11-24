from animal import Animal

def test_animal_name():
    a = Animal("Test", "TestSpecies", 2, "Food")
    assert a.get_name() == "Test"

def test_animal_health():
    a = Animal("Test", "TestSpecies", 2, "Food")
    assert a.is_healthy() is True

    