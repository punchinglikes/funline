from sys import *
import random
prefix = "funline >"
def action():
    action = input(prefix)
    return action
ca = 'Blank'
while ca == 'Blank':
    ca = action()

while ca != 'Blank':
    if ca == 'test':
        print('This works!')
        ca = action()