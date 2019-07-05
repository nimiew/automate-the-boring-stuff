#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each country

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by Census Tract']
countyData = {}

# Fill in countyData with each county's population and tracts
print('Reading rows...')
for i in range(2, sheet.max_row + 1):
    # Each row in spreadsheet has data for one census tract
    state = sheet['B' + str(i)].value
    county = sheet['C' + str(i)].value
    pop = sheet['D' + str(i)].value

    #set defaults
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write contents of countyData to it
print('Writing results...')
with open('census2010.py', 'w') as resultFile:
    resultFile.write('allData = ' + pprint.pformat(countyData))
print('Done.')
