from sys import *
import random
prefix = "funline >"
verson = "1.0.0"
def action():
    print(' ')
    action = input(prefix)
    print(' ')
    return action
ca = 'Blank'
while ca == 'Blank':    
    ca = action()
while ca != 'Blank':
    if ca == 'test':
        print('This works!')
        ca = action()
    elif ca == "help":
        print("Here are all of the commands")
        print("help :: shows this message")
        print("prefixchange :: change the prefix")
        print("test :: make sure everything is working.")
        ca = action()
    elif ca == "prefixchange":
        request = input("What would you like to change the prefix to?: ")
        prefix = request
        print('Prefix changed to "' + prefix + '"')
        ca = action()
    elif ca == "quit":
        answer = input("Are you sure you want to quit [y/n]: ")
        if answer == 'y':
            quit()
        else:
            ca = action()
    else:
        print('Unknown command, please try again.')
        ca = action()