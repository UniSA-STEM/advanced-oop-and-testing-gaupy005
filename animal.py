'''
File: animal.py
Description: Handles animal data and behaviour for the zoo system.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Animal:
    def __init__(self, name, species, age, diet_type):
        self._name = name
        self._species = species
        self._age = age
        self._diet_type = diet_type
        self._health_issues = []

    # Used Getter method
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def make_sound(self):
        return self._name + " makes a sound"

    def eat(self):
        return self._name + " is eating " + self._diet_type + " food"

    def sleep(self):
        return self._name + " is sleeping"

    def add_health_issue(self, issue):
        self._health_issues.append(issue)

    def is_healthy(self):
        return self._health_issues == []

