#! python3
# removeCSVHeader.py - removes header from all CSV files in a given dir

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file
for file in os.listdir('.\removeCsvHeader'):
    if file.endswith('.csv'):
        print('Removing header from ' + file + '...')

        # Read CSV file
        csvRows = []
        csvFileObj = open(file)
        readerObj = csv.reader(csvFileObj)

        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)
        csvFileObj.close()

        # Write out CSV file
        csvFileObj = open(os.path.join('headerRemoved', file), 'w', newline='')
        csvWriter = csv.writer(csvFileObj)

        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()
