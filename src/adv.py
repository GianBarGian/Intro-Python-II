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
move = ''
while move != 'q':

    print(f'\n{player.name} you are at {player.room.name}\n')
    print(player.room.description)
    move = input('Where do you want to go? n/s/w/e (q for quit the game): ')
    if move == 'q':
        print('Thanks for playing this game')
    elif move != 'n' and move != 's' and move != 'w' and move != 'e':
        print('Pease insert a valid direction (or q to quit)')
    elif move == 'n' and player.room.n_to:
        player.room = player.room.n_to
        print('\nYou moved north')
    elif move == 's' and player.room.s_to:
        player.room = player.room.s_to
        print('\nYou moved south')
    elif move == 'e' and player.room.e_to:
        player.room = player.room.e_to
        print('\nYou moved east')
    elif move == 'w' and player.room.w_to:
        player.room = player.room.w_to
        print('\nYou moved west')
    else:
        print('\nThere is nothing there, try another direction')
