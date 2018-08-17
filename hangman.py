
word="zombie"

def update_dashes(dashes,word,guess):
    for i in range(len(word)):
        if word[i]==guess:
            dashes=dashes[:i]+guess+dashes[i+1:]
    return dashes

def get_guess():
    while True:
        guess= input("enter a lowercase character: ")
        if len(guess) > 1:
            print ("one letter pls")
        elif not guess.islower():
            print ("your guess needs to be lowercase bby")
        else:
            break
    return guess


dashes= " "
for i in range (len(word)-1):
    dashes = dashes+"-"
misses=10

while misses>0:
    print (dashes)
    letter=get_guess()
    print (letter)
    if letter in word:
        print (letter + " is in the word")
        print ("u have " + str(misses) + " guesses left!")
        dashes=update_dashes(dashes,word,letter)
        if dashes==word:
            print ("wow hey u won wow")
            print ("good bye.")
            break

    else:
        misses=misses-1
        print (letter+ " isnt in the word")
        print ("u have " + str(misses) + " guesses left")
