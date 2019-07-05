#! python3
# readCSV.py - reads CSV file in a given dir

import csv, os, pprint

print("Select a .csv file from the following:")
pprint.pprint(os.listdir('.'))

file = str(input('Input file name: e.g. - test.csv\n'))

def testCSV(file):
    if file.endswith('.csv'):
        print('Reading ' + file + '...')
        inputFile = open(file)
        reader = csv.reader(inputFile)
        data = list(reader)
        print('Printing data[1][1] - Cell in Row 1 Column 1:\n' + data[1][1])

testCSV(file)
