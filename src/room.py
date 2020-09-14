# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items: List[Item] = []
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""

    def get_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item: Item):
        self.items.remove(item)

    def room_items(self):
        if len(self.items) > 0:
            print("This room currently has:")
            for i in self.items:
                print(f'{i.name} - "{i.description}"')

    def __str__(self):
        output = f"\nYou are in Room: {self.name} - '{self.description}'"
        return output  
