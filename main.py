from sys import *
import random
prefix = "funline >"
version = "1.0.0"
ca = 'Blank'
last = 'Nothing'
def action():
    print(' ')
    action = input(prefix)
    print(' ')

    return action

while ca == 'Blank':    
    ca = action()

while ca != 'Blank':

    if ca == 'test':
        last = 'test'
        print('This works!')
        ca = action()

    elif ca == "help":
        last = 'help'
        print("Here are all of the commands")
        print("help :: shows this message")
        print('version :: show program version')
        print("prefixchange :: change the prefix")
        print("test :: make sure everything is working.")
        print("quit :: quit the program")
        print("endlessloading :: show a endless loading screen")
        print('guess :: guess the number')
        print('last :: show the last command entered')
        ca = action()

    elif ca == "prefixchange":
        last = 'prefixchange'
        request = input("What would you like to change the prefix to?: ")
        prefix = request
        print('Prefix changed to "' + prefix + '"')
        ca = action()

    elif ca == "quit":
        last = 'quit'
        answer = input("Are you sure you want to quit [y/n]: ")
        if answer == 'y':
            quit()
        else:
            ca = action()

    elif ca == 'endlessloading':
        last = 'endlessloading'
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

    elif ca == 'guess':
        last = 'quess'
        lives = 5 #Will come later in the version
        guess = input('Im thinking of a number 1 through 100: ')
        answer = random.randint(1, 100)
        if guess == answer:
            print('Congradulations! You got it correct! Returning to the main screen.')
            ca = action()
        else:
            print('Sorry, You got it wrong. Going back to main screen.')
            ca = action()

    elif ca == 'version':
        last = 'version'
        print(version)
        ca = action()

    elif ca == 'last':
        print('The last command entered was: ' + last)
        last = 'last'
        ca = action()

    else:
        last = ca
        print('Unknown command, please try again.')
        ca = action()