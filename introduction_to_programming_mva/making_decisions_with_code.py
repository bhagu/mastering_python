'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to make decisions with code
'''

userInput = input('Enter a number: ')

if int(userInput) % 2 == 0:
    print('{0:s} is an even number'.format(userInput))
else:
    print('{0:s} is an odd number'.format(userInput))
