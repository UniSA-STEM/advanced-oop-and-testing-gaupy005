"""
File: bird.py
Description: birds in the zoo.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
"""


from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet_type, beak_length):
        super().__init__(name, species, age, diet_type)
        self._beak_length = beak_length

    def get_beak_length(self):
        return self._beak_length

    def make_sound(self):
        return self._name + " quack"