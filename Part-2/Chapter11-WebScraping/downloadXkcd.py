#! python3
# downloadXkcd.py - downloads every XKCD comic

import requests, os, bs4

url = 'http://xkcd.com' #XKCD url
os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd
#exist_ok=True -> prevents exception if folder exists already

while not url.endswith('#'):
    #downloads page
    print('Downloading page %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text) #parse HTML of the page: res

    #finds URL of comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicURL = comicElem[0].get('src')
        comicURL = 'http:' + comicURL

        #downloads image
        print('Downloading image %s...' % (comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()

    #saves image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #gets previous button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.\n')
