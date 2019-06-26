#! python3
'''
mapIt.py - Launches a map in the browser using address passed in from
command line or clipboard
'''

import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
