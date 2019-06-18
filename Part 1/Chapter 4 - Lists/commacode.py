'''
practice question for chapter 4
'''

def printSpam(spam):
    string = ''
    for i in range(len(spam)-1):
        string += spam[i]
        string += ', '

    last_item = 'and ' + spam[-1]
    string += last_item

    print(string)

spam = []

while True:
    input_str = input("Enter an object. Input nothing to stop.")
    if input_str == '':
        break
    else:
        spam.append(input_str)

printSpam(spam)
