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