estions = ["What do you call a fish without eyes?", "What is the biggest lie in the entire universe?", "Why should you stand in the corner if you get cold?", "What do you call a snowman in July?", "Why does Snoop Dog need an unbrella?", "What did Jay-Z call his wife before they got married?", "When do you go at red and stop at green?"]
jokeanswers = ["fsh", "i have read and agree to the terms and conditions", "because it's always 90 degrees", "a puddle", "fo'drizzle", "feyonce", "when you're eating a watermelon"]

def howareyou():
    print("Hey, what's your name?")
    myName = input()
    print("Well", myName, "how are you?")
    response = input()
    print("That's great!")


def main():
    howareyou()
    print("Hey, wanna hear a joke?")
    answer = input()
    if answer == "yes":
        print("Pick a number from 0 to 6: ")
        number = input()
        number = int(number)
        if number <= 6 and number >= 0:
            for i in range(len(jokequestions)):
                print(jokequestions[number])
                user_input = input()
                if user_input == jokeanswers[number]:
                    print ("wow u got it!")
                else:
                    print(jokeanswers[number])
                break
        else:
            print("Pick a number from 0 to 6 only please!")
    elif answer == "no":
        print("alright then why are you here.")

    print("kay bye.")

if __name__ == "__main__":
  main()
