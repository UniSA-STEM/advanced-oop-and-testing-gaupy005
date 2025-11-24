'''
File: animal.py
Description: Handles animal data and behaviour for the zoo system.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from health_record import HealthRecord

class Animal:
    def __init__(self, name, species, age, diet_type):
        if age < 0:
            raise ValueError("Age cannot be less than 0")
        self._name = name
        self._species = species
        self._age = age
        self._diet_type = diet_type
        self._health_records = []

    # Getter methods
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

    # this creates health record function
    def add_health_record(self, record: HealthRecord):
        self._health_records.append(record)

    def list_health_records(self):
        for record in self._health_records:
            print("- " + record.get_description())

    def is_healthy(self):
        return self._health_records == []