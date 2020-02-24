# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} is in {self.current_room}'

    def move(self, new_room):
        print(f'\n{self.name} has changed rooms...')
        self.current_room = new_room

    def get_item(self, item):
        for x in self.current_room.items:

            if x.name.upper() == item:
                self.current_room.remove_item(x)
                self.inventory.append(x)
                print(f'\n{self.name} has picked up the {x.name}')

            else:
                print("That item doesn't exist in this room.")

    def drop_item(self, item):
        for x in self.inventory:

            if x.name.upper() == item:
                self.inventory.remove(x)
                self.current_room.add_item(x)
                print(f'\n{self.name} has dropped the {x.name}')

            else:
                print("That item doesn't exist in your inventory.")
