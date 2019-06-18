import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) #adds in char as key if not already one, else nothing
    count[character] += 1 #increment count

pprint.pprint(count)
