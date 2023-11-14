#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self._name = None  # Use a private attribute to store the name
        self.name = name  # Use the property setter to validate and set the name
        self._job = None  # Use a private attribute to store the job
        self.job = job 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    # @job.setter
    def job(self, value):
        if value not in self.APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value