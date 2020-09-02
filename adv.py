from room import Room
from player import Player

# Declare all the rooms

room = {
    'Garden':  Room("Garden Gate",
                     """You stand in a small garden. To the south lies a large iron fence with a beautifully adorned gate. The path you are on leads north to a cottage"""),

    'Cottage':  Room("Cute Cottage", """The cottage is one large room with a cot, a chest, and a comfortable looking kitchen nook"""),

    'Clearing': Room("Mushroom Valley", """A vast miles-long valley lays before you. Right at your feet you see a circle of mushrooms large enough to stand in"""),

    'Beach':   Room("Beautiful Beach", """You walk along the beach and smell salt in the air. A small garden shed sits locked."""),

    'Forest': Room("Deep Dark Forest", """The air is murky here and its too dark to see a path, you must go back"""),
}


# Link rooms together
#idea, could these be set to a function and randomized? Could it be possible to create 'rare' rooms and 'frequent' ones but make it so that there is no way to predict which room you will be in next no matter what direction you go?
#Another idea: Perhaps creating a weighted function that counts the number of times you go a specific direction,(perhaps an attribute of player) maybe call the 'directions' you go 'moralities' and then that decides which room you enter.... 

room['Garden'].n_to = room['Cottage']
room['Garden'].s_to = room['Clearing']
room['Garden'].w_to = room['Beach']
room['Garden'].e_to = room['Forest']
room['Cottage'].s_to = room['Garden']
room['Beach'].e_to = room['Garden']
room['Forest'].w_to = room['Garden']
room['Clearing'].n_to = room['Garden']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
