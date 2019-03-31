from sys import *
import random
prefix = "funline >"
version = "1.0.0"
ca = 'Blank'

def action():
    print(' ')
    action = input(prefix)
    print(' ')

    return action

while ca == 'Blank':    
    ca = action()

while ca != 'Blank':

    if ca == 'test':
        print('This works!')
        ca = action()

    elif ca == "help":
        print("Here are all of the commands")
        print("help :: shows this message")
        print('version :: show program version')
        print("prefixchange :: change the prefix")
        print("test :: make sure everything is working.")
        print("quit :: quit the program")
        print("endlessloading :: show a endless loading screen")

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

    elif ca == 'endlessloading':
        percent = random.randint(1, 99)
        if percent < 25:
            print("[###----------------] " + str(percent) + "%")
        elif percent < 50 and percent > 25:
            print('[########-----------] ' + str(percent) + '%')
        elif percent < 75 and percent > 50:
            print("[###############----] " + str(percent) + '%')
        elif percent < 100 and percent > 75:
            print('[##################-] ' + str(percent) + '%')
        answer = input('Just type "quit" when you would like to leave: ')
        if answer == 'quit':
            ca = action()

        else:
            print('Wrong response, but I will assume that you wish to leave this boring screen.')
            ca = action()

    elif ca == 'version':
        print(version)
        ca = action()

    else:
        print('Unknown command, please try again.')
        ca = action()