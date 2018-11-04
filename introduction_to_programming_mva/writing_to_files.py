'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to handle files
'''

fileName = 'demo.txt'
# defining the accessmode variables
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'

myFile = open(fileName, WRITE)
myFile.write('This file has been created as part of the MVP training\n')
myFile.write('Name of the program is Introduction to Programming using Python\n')
myFile.write('The training is good!\n')
myFile.close()

print('successful!')
