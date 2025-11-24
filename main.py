'''
File: main.py
Description: Runs and demonstrates the zoo management system.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from staff import Staff
from health_record import HealthRecord
from schedule import Schedule

print("=== Prince's Zoo Simulation ===")

# create an animal
tiger = Animal("Liger", "Tiger", 8, "Meat")
print("Animal created:", tiger.get_name())

# create an enclosure
den = Enclosure("Large", "Tiger Habitat")
print("Enclosure created:", den.get_environment_type())

# test cleanliness
print("Cleanliness:", den.get_cleanliness())
den.make_dirty()
print("After dirtying:", den.get_cleanliness())
den.clean()
print("After cleaning:", den.get_cleanliness())

# add animal to enclosure
den.add_animal(tiger)

# list animals in enclosure
print("Animals in enclosure: ", end="")
den.list_animals()

# create staff
keeper = Staff("Prince", "Zookeeper")
print("Staff created:", keeper.get_name())

# staff actions
keeper.feed_animal(tiger)
keeper.clean_enclosure(den)
keeper.check_health(tiger)

record = HealthRecord("Minor injury", "2025-11-23", "Low", "Rest given")
tiger.add_health_record(record)

print("Health Records:")
tiger.list_health_records()

schedule = Schedule()
schedule.add_task("Feed animals")
schedule.add_task("Clean enclosure")

print("Today's tasks:")
schedule.list_tasks()

print("=== Demo Finished ===")