import json
from pprint import pprint


# Open a json file and append entries to the file.
f = open("allanswers.json", "r")
data = json.load(f)
print(type(data))
print(data)
f.close()

# TODO: Your code below! Analyze something interesting about your data :)

age = []
for s in range(len(data)):
    age.append(int(data[s]['age']))

print(age)
total = sum(age)
average = total/len(age)

print (average)

count = 0
oppcount = 0
for s in data:
    if s['color'] == "red":
        count += 1
    else:
        oppcount += 1
print("Who likes red?  " + str(count))
print("Who likes the other colors?  " + str(oppcount))
