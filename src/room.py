# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item

class Room:
    def __init__(self, name, description, items: List[Item]=[]):
        self.name = name
        self.description = description
        self.items: List[Item] = []
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""

    def __str__(self):
        output = f"\nRoom Name: '{self.name}'\n\nRoom Description: '{self.description}'\n\nItems: {self.items}'"
        return output   