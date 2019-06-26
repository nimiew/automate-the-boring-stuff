#! python3
# phoneAndEmail.py - finds phone no. and email addresses from clipboard text
''' TEST
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Instagram
Pinterest
'''

import pyperclip, re

#phone Regex (US)
#Encase whole regex expression in (), so groups[0] is the whole matched expression
#for easy access
phoneRegex = re.compile(r'''(
    (\d{3}|\(\+\d{3}\))? # country code
    (\s|-|\.)? # separator - remember to escape s and .
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)

#email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Clipboard
text = str(pyperclip.paste())
matches = []
#format the phone numbers properly
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !='':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

#Join to clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
