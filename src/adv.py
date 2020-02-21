from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

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
    print(f'\nLocation: {PLAYER.current_room.name}')

    # * Prints the current description (the textwrap module might be useful here).
    print(f'Description: {PLAYER.current_room.description}')

    # * Waits for user input and decides what to do.
    INPUT_CMD = input("\nWhere would you like to go: ").split(' ')

    # TODO: handle multiple args
    COMMAND = INPUT_CMD[0] # Store single command for now

    # If the user enters a cardinal direction, attempt to move to the room there.

    # Check command val and make it uppercase for
    # consistency
    if COMMAND.upper() == "N" or COMMAND.upper() == "S" or COMMAND.upper() == "E" or COMMAND.upper() == "W":
        # use direction method to get new room
        MOVE_TO_ROOM = PLAYER.current_room.direction(COMMAND.upper())

        # if val of MOVE_TO_ROOM is None
        if MOVE_TO_ROOM == None:
            print("\nYou cannot move in that direction!")
        else:
            # else change the Player's location
            PLAYER.move(MOVE_TO_ROOM)

    # Else (if not N, S, E, or W), invalid command
    else:
        print("\nYou cannot move in that direction!")

    # If command is "Q" break the loop
    if COMMAND.upper() == "Q":
        print("\nThanks for playing!\n")
        break

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
