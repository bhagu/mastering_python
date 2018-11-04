'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to repeat events
'''

import turtle
turtle.color('green')
userInput = input('Enter the number of times the loop should get executed: ')
for steps in range(int(userInput)):
    turtle.forward(100)
    turtle.right(360/int(userInput))
    for moresteps in range(int(userInput)):
        turtle.forward(50)
        turtle.right(360/int(userInput))


