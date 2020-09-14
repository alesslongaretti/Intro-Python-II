# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def change_room(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room != "":
            self.room = next_room
        else:
            output = "\nYou cannot enter this room!\n"
            print(output)

    def get_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item):
        self.items.remove(item)

    def player_items(self):
        if len(self.items) > 0:
            print("\nYour inventory currently has:")
            for i in self.items:
                print(f"{i.name} - '{i.description}'\n")
        else:
            print("\nThere is nothing in your inventory.\n")

    def __str__(self):
        output = f"\n\nWelcome {self.name}!\n\n {self.room}"
        return output