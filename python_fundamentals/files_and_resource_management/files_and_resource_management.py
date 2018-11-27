import sys
print(sys.getdefaultencoding())

userFile = open('test.txt')

fileContents = userFile.read()
print(fileContents)

userFile.close()
