"""
File: schedule.py
Description: Manages simple daily tasks and schedules for zoo staff.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Schedule:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def list_tasks(self):
        for task in self._tasks:
            print("- " + task)