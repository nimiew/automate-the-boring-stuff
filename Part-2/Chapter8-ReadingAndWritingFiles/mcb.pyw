#! python3
# mcb.pyw - saves and loads multiple pieces of text to clipboard

#Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard
#       py.exe mcb.pyw list - loads all keywords to clipboard
#       py.exe mcb.pyw delete <keyword> - deletes keyword from clipboard
#       py.exe mcb.pyw delete list - deletes all keywords from clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #list keywords and content
    if sys.argv[1].lower() == 'list': #copy all
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf: #elif inside the shelf, copy it
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
