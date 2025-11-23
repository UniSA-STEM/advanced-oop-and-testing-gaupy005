"""
File: reptile.py
Description: reptiles in the zoo.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Reptile(Animal):
    # this creates a reptile using animal parent class
    def __init__(self, name, species, age, diet_type, scale_type):
        super().__init__(name, species, age, diet_type)
        self._scale_type = scale_type

    # getter for scale type
    def get_scale_type(self):
        return self._scale_type

    # polymorphism for different sound for reptiles
    def make_sound(self):
        return self._name + " makes an animal sound"