
userInput = input('Enter a number: ')

if int(userInput) % 2 == 0:
    print('{0:s} is an even number'.format(userInput))
else:
    print('{0:s} is an odd number'.format(userInput))
