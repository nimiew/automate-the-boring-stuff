import re

'''
- r is to treat string as raw string, and ignore escape chars
- re.compile() is to create Regex object
- Parentheses is to separate groups
    - group() returns whole matching text
    - group(1) returns first matching group, group(2) returns second, etc.
'''
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
#Note the brackets are being escaped for them to be matched

mo = phoneNumRegex.search('My number is (415) 555-4242.')
print('Phone number found: ' + mo.group())

'''
- '|': or (first one to match will be returned)
- '?': optional (there/not there) (0/1)
- '*': matching 0 or more (>=0)
- '+': matching 1 or more (>0 or >=1)
- '{}': matching specific number of times
    - {3}: match 3 times
    - {3, 5}: match 3 to 5 times
'''

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print('mo1.group() = ' + mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print('mo2.group() = ' + mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print('mo3.group() = ' + mo3.group())
print('mo3.group(1) = ' + mo3.group(1)) #returns first matching text in ()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My number is 415-555-4242')
print('mo4.group() = ' + mo4.group())
mo5 = phoneRegex.search('My number is 555-4242')
print('mo5.group() = ' + mo5.group())

batRegex = re.compile(r'Bat(wo)*man')
mo6 = batRegex.search('The Adventures of Batman')
print('mo6.group() = ' + mo6.group())
mo7 = batRegex.search('The Adventures of Batwoman')
print('mo7.group() = ' + mo7.group())
mo8 = batRegex.search('The Adventures of Batwowowowoman')
print('mo8.group() = ' + mo8.group())

batRegex = re.compile(r'Bat(wo)+man')
mo6 = batRegex.search('The Adventures of Batman')
print('mo6 == None?\n' + str(mo6 == None))
mo7 = batRegex.search('The Adventures of Batwoman')
print('mo7.group() = ' + mo7.group())
mo8 = batRegex.search('The Adventures of Batwowowowoman')
print('mo8.group() = ' + mo8.group())

haRegex = re.compile(r'(ha){3}')
mo1 = haRegex.search('hahaha')
print('mo1.group() = ' + mo1.group())
mo2 = haRegex.search('haha')
print('mo2 == None?\n' + str(mo2 == None))

'''
Greedy Regex matching: matches longest string possible
Non-greedy: shortest possible string match -> using '?'
'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print('mo1.group() = ' + mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print('mo2.group() = ' + mo2.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 202-555-0000'))

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

'''
Defining a character class
[asg] - matching letters 'a', 's', or 'g'
[^asg] - letters NOT matching
'''

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Hello World'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Hello World'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
