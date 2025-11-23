"""
File: mammal.py
Description: Represents mammals in the zoo.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Mammal(Animal):
    # this creates a mammal using animal parent class
    def __init__(self, name, species, age, diet_type, fur_color):
        super().__init__(name, species, age, diet_type)
        self._fur_color = fur_color

    # getter for fur color
    def get_fur_color(self):
        return self._fur_color


