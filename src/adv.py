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

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

hat = Item('Hat', 'a comfortable hat')
sword = Item('Sword', 'a sword to slay monsters')
shield = Item('Shield', 'a shield to protect yourself')
boots = Item('Boots', 'a pair of boots to protect yourself from cold')
ring = Item('Ring', 'a magic ring. What will it do?')
armor = Item('Armor', 'a fine armor to protect yourself')

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Add items to rooms
room['outside'].items = [hat, boots]
room['foyer'].items = [armor]
room['overlook'].items = [ring]
room['narrow'].items = [sword, shield]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please provide a name for your character: ')
player = Player(name, room['outside'])
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
move = [""]
while move[0] != 'q':
    if move[0] != "no repeat":
        print(f'\n{player.name} you are at {player.room.name}\n')
        print(player.room.description)
    move = input('\nWhere do you want to go? n/s/w/e (q for quit the game): ')
    move = move.strip().split(' ')
    if len(move) == 1:
        if move[0] == 'q':
            print('Thanks for playing this game')
        elif move[0] != 'n' and move[0] != 's' and move[0] != 'w' and move[0] != 'e' and move[0] != 'inspect' and move[0] != 'inventory' and move[0] != 'i' :
            print('Pease insert a valid direction (or q to quit)')
            move[0] = "no repeat"
        elif move[0] == 'n' and player.room.n_to:
            player.room = player.room.n_to
            print('\nYou moved north')
        elif move[0] == 's' and player.room.s_to:
            player.room = player.room.s_to
            print('\nYou moved south')
        elif move[0] == 'e' and player.room.e_to:
            player.room = player.room.e_to
            print('\nYou moved east')
        elif move[0] == 'w' and player.room.w_to:
            player.room = player.room.w_to
            print('\nYou moved west')
        elif move[0] == 'inspect':
            player.room.inspect()
            move = "no repeat"
        elif move[0] == 'i' or move[0] == 'inventory':
            print('Inventory:')
            for item in player.inventory:
                print(f'  -{item.name}')
            move[0] = "no repeat"
        else:
            print('\nThere is nothing there, try another direction')
            move[0] = "no repeat"
    else:
        if move[0] == 'take':
            item_exist = list(filter(lambda item: item.name == move[1], player.room.items))
            if len(item_exist) > 0:
                item = item_exist[0]
                player.room.items.remove(item)
                player.inventory.append(item)
                item.on_take(item.name)
            else:
                print('That item is not here!')
        if move[0] == 'drop':
            item_exist = list(filter(lambda item: item.name == move[1], player.inventory))
            if len(item_exist) > 0:
                item = item_exist[0]
                player.room.items.append(item)
                player.inventory.remove(item)
                item.on_drop(item.name)
            else:
                print('That item is not here!')
        move[0] = "no repeat"
        


                    

