# --- Define your functions below! ---
def intro():
    print("Hi! I'm chatboi!")

def response():
    if answer == "hi!":
        print("What's good?")
    else:
        print("That's cool!")


# --- Put your main program below! ---
def main():
    intro()
    while True:
      answer = input("(What will you say?)")
      response()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
