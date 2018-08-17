#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords


#Write logic to see if the password is in the dictionary file below here:
#if test_password == line in f:
    #print("Your password is wack.")
#else:
    #("It's aii.")
test_password = input("Type in a trial password: ")
test_password = test_password.lower()
password = "weak password"
#if password == "weak password"
for i in f:
    if test_password.strip() == i.strip():
        password ="weak password"
        break
    else:
        password = "strong password"
print (password)
