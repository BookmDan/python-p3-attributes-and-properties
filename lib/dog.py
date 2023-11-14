#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name="", breed="default", age=None):
        self.name = name
        self.breed = breed
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print(f"Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS :
            print(f"Breed must be in the list of approved breeds.")
        else:
            self._breed = breed


    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
