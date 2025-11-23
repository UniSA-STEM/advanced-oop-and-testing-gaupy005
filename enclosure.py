'''
File: enclosure.py
Description: Manages animal enclosures and their conditions.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    # this creates an enclosure with a size and environment type
    def __init__(self, size, environment_type):
        self._size = size
        self._environment_type = environment_type
        self._animals = []
        self._cleanliness = 100  # when it's 100 it's fully clean

    # getter for size
    def get_size(self):
        return self._size

    # getter for environmental type
    def get_environment_type(self):
        return self._environment_type

    # getter for cleanliness
    def get_cleanliness(self):
        return self._cleanliness

    # this makes enclosure dirty
    def make_dirty(self):
        self._cleanliness -= 10

    # this cleans the enclosure
    def clean(self):
        self._cleanliness = 100

    # this adds an animal to their environmental needs
    def add_animal(self, animal):
        if self._environment_type.lower() not in animal.get_species().lower():
            print("Wrong environment for this animal.")
            return

        self._animals.append(animal)
        print(animal.get_name() + " added to enclosure.")

    # this removes an animal by name
    def remove_animal(self, animal_name):
        for animal in self._animals:
            if animal.get_name().lower() == animal_name.lower():
                self._animals.remove(animal)
                print(animal_name + " removed from enclosure.")
                return
        print(animal_name + " not found in enclosure.")

    # this lists all animals in this enclosure
    def list_animals(self):
        for animal in self._animals:
            print("- " + animal.get_name())
