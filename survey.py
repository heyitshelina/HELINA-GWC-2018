import json
#friends = {
 # "Tasfia": 16,
  #"Mo": 16,
  #}

#friendAge = friends["Mo"]
#print (friendAge)

#user = {}

#user['Diana'] = 30
#print (user)
#user['Amy'] = 27
#print (user)

# TODO Part I: Add your survey questions to this empty list.
survey = [
    "What is your favorite color?",
    "How old are you?",
    "Who is your favorite artist/band?",
    "What is your favorite food?",
    "What is your favorite sport?"
    ]

# TODO Part I: store the related keys corresponding to the survey answers here.
keys = [
    "color",
    "age",
    "music",
    "food",
    "sport"
    ]
# Create a list that will store each person's individual survey responses.
# Use for Part II.
list_of_answers = []

# Creates the dictionary to store responses.


while True:
    answers = {}
    for i in range(len(survey)):
        response = input(survey[i] + " ")
        answers[keys[i]] = response
    list_of_answers.append(answers)
    print ("Are there more users?")
    user_input = input()
    if user_input == "no":
        print("Okay thanks!")
        break



# TODO Part I: write code that asks each survey question and prompts the user for a response.
# Hint: how can you go through each element of a list?



# Print the context of the dictionary.
print(list_of_answers)

"""
This code should be pasted after the code you have previously written! Do NOT delete your older code!!!!
Before running this code, be sure to open a new Atom file. Make the file contain only [] and save it as allanswers.json.
"""

# Open the file containing all past results and append them to our current list.
f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

# Reopen the file in write mode and write each entry in json format.
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if (index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
