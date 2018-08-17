def say_hello(name):
    print("Hi "+ name)

def user_response(feeling):
    print ("Oh, I am", feeling, "too.")

def main():
    user = "Helina"
    say_hello(user)
    feeling =  input("How are you doing today?")
    user_response(feeling)

if __name__ == "__main__":
  main()
