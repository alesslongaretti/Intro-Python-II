# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        output = f"{self.name} is in room {self.room}"
        return output

    def change_room(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room != "":
            self.room = next_room
        else:
            output = "\nYou cannot enter this room!\n"
            print(output)
