from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),


    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'lagoon': Room("Grand Lagoon", """You fell into the dark lagoon. Go back to the south, Grand Overlook or go North to cross
the uncrossable bridge"""),

    'bridge': Room("Uncrossable Bridge", """uh oh! This is the uncrossable bride, therfore you cannot cross it!. Go back to the 
    lagoon to find your way out"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),


    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['lagoon']
room['lagoon'].s_to = room['overlook']
room['lagoon'].n_to = room['bridge']
room['bridge'].s_to = room['lagoon']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


room['outside'].items.append(Item("Armor", "protective covering for a warrior"))
room['outside'].items.append(Item("Map", "diagrammatic representation of the land for a warrior"))
room['outside'].items.append(Item("Pen", "writing instrument to make notes on the map for a warrior"))
room['foyer'].items.append(Item("Shield", "a broad piece of metal used for protection for a warrior"))
room['foyer'].items.append(Item("Water", "drinkable liquid for a warrior"))
room['overlook'].items.append(Item("Sword", "a weapon with a long metal blade for a warrior"))
room['overlook'].items.append(Item("Boots", "footwear for a warrior"))
room['narrow'].items.append(Item("Cape", "a cloak for a warrior"))
room['narrow'].items.append(Item("Rock", "a weapon for a warrior"))
room['treasure'].items.append(Item("Key", "key to the treasure for a warrior"))




# Make a new player object that is currently in the 'outside' room.

new_player = Player('ale', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ["n", "s", "e", "w"]

while True:
    print(f'\n{new_player}')
    user_input = input("\nWhere would you want to go (n,s,e or w)? Type q to quit the game: ")
    split_input = user_input.split()

    if user_input == "q":
        print("*** Game Over! ***")
        break
    elif user_input in directions:
        new_player.change_room(user_input)
    elif user_input == "i" or user_input == "inventory":
        new_player.player_items()
    elif len(split_input) == 2:
        item_name = split_input[1]
        if split_input[0].lower() == "get":
            item = new_player.room.get_item(item_name)
            if item:
                item.on_take()
                new_player.room.remove_item(item)
                new_player.items.append(item)
                new_player.room.room_items()
            else:
                print(f"\n{item_name} does not exist in room")
        elif split_input[0].lower() == "drop":
            item = new_player.get_item(item_name)
            if item:
                item.on_drop()
                # remove the item from the player
                new_player.remove_item(item)
                # Add it to the room's items
                new_player.room.items.append(item)
                new_player.player_items()
                new_player.room.room_items()
            else:
                print(f"\n{item_name} does not exist in room")
    else:
        print("\nINVALID INPUT, TRY AGAIN!\n")

