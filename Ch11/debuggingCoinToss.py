import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
#toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = 0
if toss == 0:
    tossResult = 'tails'
else:
    tossResult = 'heads'
if tossResult == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if tossResult == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')