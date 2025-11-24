from animal import Animal

def test_animal_name():
    a = Animal("Test", "TestSpecies", 2, "Food")
    assert a.get_name() == "Test"