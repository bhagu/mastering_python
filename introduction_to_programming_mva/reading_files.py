'''
    This script has been created as part of the introduction to python training by microsoft virtual academy
    This section covers how to read from files
'''

fileName = 'demo.txt'
# defining the accessmode variables
WRITE = 'w'
READ = 'r'
APPEND = 'a'
READWRITE = 'w+'

myFile = open(fileName, READ)
allFileContents = myFile.read()
# point the string to the first index
myFile.seek(0)
allFileContents2 = myFile.read()
# if we have executed this without the seek command, we would have gotten empty string
myFile.close()

print(allFileContents)
print(allFileContents2)






