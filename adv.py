from room import Room
from player import Player

# Declare all the rooms

room = {
    'Garden':  Room("Garden Gate",
                     """You stand in a small garden. To the south lies a large iron fence with a beautifully adorned gate. The path you are on leads north to a cottage"""),

    'Cottage':  Room("Cute Cottage", """The cottage is one large room with a cot, a chest, and a comfortable looking kitchen nook"""),

    'Clearing': Room("Mushroom Valley", """A vast miles-long valley lays before you. Right at your feet you see a circle of mushrooms large enough to stand in"""),

    'Beach':   Room("Beautiful Beach", """You walk along the beach and smell salt in the air. A small garden shed sits locked."""),

    'Forest': Room("Deep Dark Forest", """The air is murky here and its too dark to see a path, you should go back"""),

    'Forest2': Room("Deeper Darker Forest","""It has now gotten too hard for you to see and the air has gotten colder. You feel around in the branches and grab hold of a tree. Go back before it is too late"""),

    'Forest3': Room("Deepest Darkest Forest","""You have been eaten by wolves.""")

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
room['Forest'].e_to = room['Forest2']
room['Forest2'].w_to = room['Forest']
room['Forest2'].e_to = room['Forest3']
room['Clearing'].n_to = room['Garden']


#
#

# Make a new player object that is currently in the 'outside' room. 
print("Welcome to Garden House! The most normal place in the world. Nothing ever happens here-- making it a fantastic spot for quiet contemplation and gardening.")
x = input("I'm Zabkadabka. Whats your name? ")

lostchild= Player(x,room['Garden']);

print(f'Nice to mee you {x}! Remember the aim is to Garden ')

#x = input("Which way would you like to go? n, s, w, e : ")

# Write a loop that:
codeword='play on'
while codeword != 'q':
    print(f'You are currently at the {lostchild.current_room.name}')
    print(lostchild.current_room.description)
    codeword = input("Which way would you like to go? n, s, w, e : ")
    if codeword == 'n':
        if lostchild.current_room.n_to != 'null' :
            lostchild.current_room=lostchild.current_room.n_to;
        else:
            print("~There is no Path in that direction~");
    elif codeword == 's':
        if lostchild.current_room.s_to != 'null':
            lostchild.current_room=lostchild.current_room.s_to;
        else:
            print("~There is no Path in that direction~");
    elif codeword == 'e':
        if lostchild.current_room.e_to != 'null':
            lostchild.current_room=lostchild.current_room.e_to;
        else:
            print("~There is no Path in that direction~");
    elif codeword == 'w':
        if lostchild.current_room.w_to != 'null':
            lostchild.current_room=lostchild.current_room.w_to;
        else:
            print("~There is no Path in that direction~");

    else:
        print("~That is an invalid input~");
    if lostchild.current_room.name == "Deepest Darkest Forest":
        print(lostchild.current_room.description)
        codeword = 'q';
        

print("Thanks for playing!")
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
