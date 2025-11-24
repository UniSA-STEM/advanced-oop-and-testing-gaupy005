'''
File: zoo_report.py
Description: It's a zoo reporting system
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
'''

class ZooReport:
    # this lists all animals by species
    def list_animals_by_species(self, animals):
        for animal in animals:
            print(animal.get_species() + " - " + animal.get_name())

    # this prints enclosure cleanliness level
    def report_enclosure(self, enclosure):
        print("Cleanliness:", enclosure.get_cleanliness())