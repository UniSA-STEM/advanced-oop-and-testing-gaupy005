'''
File: staff.py
Description: Stores staff roles and their duties in the zoo.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Staff:
    # this creates a staff member with a name and role
    def __init__(self, name, role):
        self._name = name
        self._role = role

    # getter for name
    def get_name(self):
        return self._name

    # getter for role
    def get_role(self):
        return self._role

    # this makes the staff member feed an animal
    def feed_animal(self, animal):
        print(self._name + " fed " + animal.get_name())

    # this makes the staff member clean an enclosure
    def clean_enclosure(self, enclosure):
        print(self._name + " cleaned the enclosure.")

    # this makes the vet check an animal
    def check_health(self, animal):
        if animal.is_healthy():
            print(animal.get_name() + " is healthy.")
        else:
            print(animal.get_name() + " has health issues.")