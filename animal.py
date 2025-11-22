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
        self.name = name
        self.species = species
        self.age = age
        self.diet_type = diet_type
        self.health_issues = []

    def make_sound(self):
        return self.name + " makes a sound"

    def eat(self):
        return self.name + " is eating " + self.diet_type + " food"

    def sleep(self):
        return self.name + " is sleeping"

    def add_health_issue(self, issue):
        self.health_issues.append(issue)

    def is_healthy(self):
        return self.health_issues == []

