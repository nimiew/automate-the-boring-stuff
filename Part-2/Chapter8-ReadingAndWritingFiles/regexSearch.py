'''
regexSearch.py - searches for given input in .txt files in a given folder
'''

import re, os

path = input('Enter folder you wish to search in. e.g. \'D:\\Codes\Python\'\n')
keyword = input('Enter the keyword you wish to search for. e.g. hehe\n')
keywordRegex = re.compile(r'({})'.format(keyword), re.IGNORECASE)
matches = []
count = 0;

for file in os.listdir(path):
    if file.endswith('.txt'):
        with open(os.path.join(path, file)) as txtFile:
            #Regex handling
            text = txtFile.read()
            for group in keywordRegex.findall(text):
                matches.append("{}: Found '{}' in {}\n".format(count+1, group, file))
                count+=1

if len(matches)>0:
    print("Matches found:\n")
    print('\n'.join(matches))

else:
    print("No matches found in {}.\n".format(path))
