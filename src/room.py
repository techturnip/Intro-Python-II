# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        output = f'Location: {self.name}\nDescription: {self.description}\nVisible Items:'
        for i in self.items:
            output += f'\n - {i}'
        return output

    def direction(self, direction):
        if direction == "N":
            return self.n_to
        elif direction == "S":
            return self.s_to
        elif direction == "E":
            return self.e_to
        elif direction == "W":
            return self.w_to
        else:
            return None

    def remove_item(self, item):
        for i in self.items:
            if i == item:
                self.items.remove(item)
                print(f'{i.name} was removed from {self.name}')

    def add_item(self, item):
        self.items.append(item)
        print(f'{item.name} hit the floor.')
