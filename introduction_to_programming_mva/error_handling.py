'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to handle errors
'''

import sys

#Accepting user inputs
firstNumber = float(input('Enter the first number: '))
secondNumber = float(input('Enter the second number: '))

try:
    result = firstNumber/secondNumber
    print('{0:.2f} / {1:.2f} = {2:.2f}'.format(firstNumber,secondNumber,result))
except ZeroDivisionError:
    print('The answer is infinity!')
except:
    error = sys.exc_info()[0]
    print('Something went wrong')
    print(error)
finally:
    print('This section gets executed everytime, irrespecitve of whether any errors are there or not')