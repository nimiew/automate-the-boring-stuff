#! python3
# lucky.py - Opens several Google search results.
#!!! Does not work - linkElems always 0. debug?

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
webbrowser.open('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select('.r a')
print(len(linkElems))
numOpen = min(5, len(linkElems)) # max of top 5 searches
print(numOpen)
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print('run?')
