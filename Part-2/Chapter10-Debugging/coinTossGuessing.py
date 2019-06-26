import random
choices = ('heads', 'tails')
guess = ''

while guess not in choices:
    print('Guess the coin toss! Enter heads or tails:')
    guess = str.lower(input())
#toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = random.choice(choices)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game. (It can only be heads or tails...?)')
