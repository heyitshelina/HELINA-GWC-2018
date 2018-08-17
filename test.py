
from random import *
number = randint(1,50)
guessesTaken = 0

print('Hello! What is your name?')
myName = input()
print('Well, ' + myName + ', take your shot at guessing my favorite number from 1 through 50.')

while guessesTaken < 3:
    print ("Give it a try: ")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    elif guess == number:
        print ("You got the right number!")
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)
