# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = None

    def inspect(self):
        print('\nAfter you searched the room you could find these items')
        for item in self.items:
            print(f'  -{item.name}: This is {item.description}')
