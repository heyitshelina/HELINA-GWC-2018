'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
tweetPolarity = []
tweetSubjectivity = []


for tweet in tweetData:
	tweetblob = TextBlob(tweet["text"])
	tweetPolarity.append(tweetblob.polarity)
	tweetSubjectivity.append(tweetblob.subjectivity)

print(tweetPolarity)
print(tweetSubjectivity)

print("Polarity Average: ")
total = sum(tweetPolarity)
average = total/len(tweetPolarity)
print (average)

print("Subjectvity Average: ")
total = sum(tweetSubjectivity)
average = total/len(tweetSubjectivity)
print (average)


import matplotlib.pyplot as plt

plt.hist(tweetPolarity, bins=[-0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
plt.xlabel('Polarity Value')
plt.ylabel('Number of Tweets')
plt.title('Tweet Polarity')
plt.axis([-1, 1.5, 0, 50])
plt.grid(True)
plt.show()
