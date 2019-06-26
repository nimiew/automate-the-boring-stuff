'''
censors/redacts NRIC numbers found in text????
Test: S9632113F
'''

import re, pyperclip

nricRegex = re.compile(r'(([stST])\d{4}(\d{3})(\w))')

text = str(pyperclip.paste())
#print(text)
redacted = []

for groups in nricRegex.findall(text):
    #print(groups)
    #print(nricRegex.sub(r'\2****\3\4', groups[0]))
    redacted.append(nricRegex.sub(r'\2****\3\4', groups[0]))

if len(redacted) > 0:
    #print(redacted)
    pyperclip.copy('\n'.join(redacted))
    print('Copied to clipboard:')
    print('\n'.join(redacted))
else:
    print('No NRIC numbers found')
