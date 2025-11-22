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

    # getter for size
    def get_size(self):
        return self._size

    # getter for environment type
    def get_environment_type(self):
        return self._environment_type
