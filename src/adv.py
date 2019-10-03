from room import Room
from player import Player
from item import Item
from light_source import Light_source
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Create items

hat = Item('Hat', 'a comfortable hat')
sword = Item('Sword', 'a sword to slay monsters')
shield = Item('Shield', 'a shield to protect yourself')
boots = Item('Boots', 'a pair of boots to protect yourself from cold')
ring = Item('Ring', 'a magic ring. What will it do?')
armor = Item('Armor', 'a fine armor to protect yourself')
torch = Light_source('Torch', 'a torch to see in the dark')

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
room['treasure'].items = [torch]


act = [""]


def action_logic(action_list):
    if len(action_list) == 1:
        single_action(action_list[0])
    elif len(action_list) == 2:
        composite_action(action_list)


def single_action(action):
    global act
    if action == 'q':
        print('Thanks for playing this game')
    elif action not in ['n', 's', 'w', 'e', 'inspect', 'inventory', 'i']:
        print('Pease insert a valid direction (or q to quit)')
        act[0] = "no repeat"
    elif action == 'n' and player.room.n_to:
        player.room = player.room.n_to
        print('\nYou moved north')
    elif action == 's' and player.room.s_to:
        player.room = player.room.s_to
        print('\nYou moved south')
    elif action == 'e' and player.room.e_to:
        player.room = player.room.e_to
        print('\nYou moved east')
    elif action == 'w' and player.room.w_to:
        player.room = player.room.w_to
        print('\nYou moved west')
    elif action == 'inspect':
        player.room.inspect()
        act[0] = "no repeat"
    elif action == 'i' or action == 'inventory':
        print('Inventory:')
        for item in player.inventory:
            print(f'  -{item.name}')
        act[0] = "no repeat"
    else:
        print('\nThere is nothing there, try another direction')
        act[0] = "no repeat"


def composite_action(action_list):
    global act
    if action_list[0] == 'take':
        item_exist = list(
            filter(lambda item: item.name == action_list[1], player.room.items))
        if len(item_exist) > 0:
            item = item_exist[0]
            player.room.items.remove(item)
            player.inventory.append(item)
            item.on_take(item.name)
        else:
            print('That item is not here!')
    if action_list[0] == 'drop':
        item_exist = list(
            filter(lambda item: item.name == action_list[1], player.inventory))
        if len(item_exist) > 0:
            item = item_exist[0]
            player.room.items.append(item)
            player.inventory.remove(item)
            item.on_drop(item.name)
        else:
            print('That item is not here!')
    act[0] = "no repeat"

def room_description(player):
    is_light_source = list(filter(lambda item: type(item).__name__ == "Light_source", player.room.items))
    if player.room.is_light or len(is_light_source) > 0:
        print(f'\n{player.name} you are at {player.room.name}\n')
        print(player.room.description)
    else:
        print('Is pitch black!')

print(type(torch).__name__)
#
# Main
#


name = input('Please provide a name for your character: ')
player = Player(name, room['outside'])
while act[0] != 'q':
    if act[0] != "no repeat":
        room_description(player)
        # print(f'\n{player.name} you are at {player.room.name}\n')
        # print(player.room.description)
    act = input('\nWhere do you want to go? n/s/w/e (q for quit the game): ')
    act = act.strip().split(' ')
    action_logic(act)
