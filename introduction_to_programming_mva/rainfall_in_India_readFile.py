
import csv

fileName = 'rainfall in india 1901-2015.csv'
accessMode = 'r'

with open(fileName, accessMode) as rainfallFile:
    # read the file contents
    dataFromFile = csv.reader(rainfallFile)
    for currentRow in dataFromFile:
        print(currentRow)

