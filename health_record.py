"""
File: health_record.py
Description: Stores and manages animal health records.
Author: Prince Gautam
Student ID: 110351192
Username: gaupy005
This is my own work as defined by the University's Academic Integrity Policy.
"""


class HealthRecord:
    # this creates a health record for an animal
    def __init__(self, description, date_reported, severity, treatment_notes):
        self._description = description
        self._date_reported = date_reported
        self._severity = severity
        self._treatment_notes = treatment_notes

    # getter for description
    def get_description(self):
        return self._description

    # getter for date
    def get_date_reported(self):
        return self._date_reported

    # getter for severity
    def get_severity(self):
        return self._severity

    # getter for treatment notes
    def get_treatment_notes(self):
        return self._treatment_notes