'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to handle numbers in python
'''

# variables used in this script
message = ''
width = 0
height = 0
area = 0
perimeter = 0

# printing the message
message = 'Calculate the area and perimeter of a rectangle!'
print (message)
print ('*' * len(message))

# acceping the user inputs
width = int(input('Enter the Width: '))
height = int(input('Enter the Height: '))

# calculating the values
area = width * height
perimeter = 2 * (width + height)

# displaying the results
print('The area of the rectangle is %d' % area)
print('The perimeter of the rectangle is %d' % perimeter)

print('\n')
# experimenting with the results
print('The area of the rectangle is %5d' % area)
print('The perimeter of the rectangle is %5d' % perimeter)

print('\n')

print('The area of the rectangle is %05d' % area)
print('The perimeter of the rectangle is %05d' % perimeter)  

print('\n')
# using format to display the results
print('The area of the rectangle is {0:d}'.format(area))
print('The area of the rectangle is {0:d}'.format(perimeter))

# format - displaying both of the results together
print('\nThe area of the rectangle is {0:d} and perimeter is {1:.2f}'.format(area, perimeter))
