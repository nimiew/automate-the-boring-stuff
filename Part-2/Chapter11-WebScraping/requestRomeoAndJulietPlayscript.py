import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as e:
    #print('Error downloading file... - {}'.format(e))
    print('Error downloading file... - %s' % (e))

with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000): #100000bytes is a reasonable amt
        playFile.write(chunk)
