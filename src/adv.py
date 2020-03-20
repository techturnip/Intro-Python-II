from room import Room
from player import Player
from item import Item

# Declare all the items
items = {
    'outside': [Item("Torch", "A lit torch"),
                Item("Rock", "What an interesting rock...")],
    'foyer': [],
    'overlook': [],
    'narrow': [],
    'treasure': [],
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items['outside']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items['foyer']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items['overlook']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['narrow']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items['treasure']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
PLAYER = Player('Tyler', room['outside'])

# START GAME
GREETING = f'Your adventure awaits, {PLAYER.name}\n'

print(GREETING, "___________________")

# Write a loop that:
while True:

    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Print a list of items
    print(f'\n{PLAYER.current_room}')

    # * Waits for user input and decides what to do.
    INPUT_CMD = input("\nEnter direction (N,E,S,W) or Command (GET/DROP ITEM): ").split(' ')

    # TODO: handle multiple args
    COMMAND = INPUT_CMD # Store single command for now

    # If the user enters a cardinal direction, attempt to move to the room there.

    # Check command val and make it uppercase for
    # consistency
    if len(COMMAND) == 1:
        SNGL_CMD = COMMAND[0].upper()


        # If the user enters "q", quit the game.
        # If command is "Q" break the loop
        if SNGL_CMD == "Q":
            print("\nThanks for playing!\n")
            break

        if SNGL_CMD == "N" or SNGL_CMD == "S" or SNGL_CMD == "E" or SNGL_CMD == "W":

            # use direction method to get new room
            MOVE_TO_ROOM = PLAYER.current_room.direction(SNGL_CMD)

            # if val of MOVE_TO_ROOM is None
            if MOVE_TO_ROOM == None:
                print("\nYou cannot move in that direction!")
            else:
                # else change the Player's location
                PLAYER.move(MOVE_TO_ROOM)

        # Print an error message if the movement isn't allowed.
        # Else (if not N, S, E, or W), invalid command
        elif SNGL_CMD != "Q":
            print("\nYou cannot move in that direction!")

    # Parse Player Actions
    elif len(COMMAND) > 1:
        if COMMAND[0].upper() == "GET":
            PLAYER.get_item(COMMAND[1].upper())
        elif COMMAND[0].upper() == "DROP":
            PLAYER.drop_item(COMMAND[1].upper())
        else:
            print("\nThat command doesn't exist...")
