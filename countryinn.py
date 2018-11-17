import got3
import nltk
from nltk.corpus import stopwords
import string
import time
import random
import matplotlib.pyplot as plt
import operator
import csv
import re

dates = []
# Create random list of 10000 dates to search in past 10 years
for i in range(0, 10000):
    year = random.randrange(2008, 2018)
    month = random.randrange(1, 13)
    day = random.randrange(1, 30)
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    dates.append(str(year) + "-" + str(month) + "-" + str(day))

# Preparing for loop run
csvData = [["Date", "Text", "Username", "Id", "Permalink", "Retweets", "Favorites"]]
words = []
counter = 0

# Perform tweet retrieval per random date
for date in dates:
    # Set the search criteria for tweets
    tweetCriteria = got3.manager.TweetCriteria() \
        .setUntil(date) \
        .setQuerySearch("country inn") \
        .setMaxTweets(1) \
        .setTopTweets(True)

    # Start retrieving tweets
    start = time.time()
    tweet = got3.manager.TweetManager.getTweets(tweetCriteria)
    end = time.time()
    counter += 1
    print(str(counter), end - start)

    # Preparing for filtering of stopwords and duplicates
    swords = stopwords.words('english')
    tweetset = set()

    # Reassigning pointer to set of no duplicates

    for i in tweet:
        tweetInfo = []
        tweetset.add(i.text) # Remove duplicate files

        # Prepare to add to csv array
        tweetInfo.append(i.date)
        tweetInfo.append(i.text)

        # Retrieve username using regular expressions
        username = re.search('https://twitter\.com/(.*)/status', i.permalink)
        username = username.group(1)
        tweetInfo.append(username)

        tweetInfo.append(i.id)
        tweetInfo.append(i.permalink)
        tweetInfo.append(i.retweets)
        tweetInfo.append(i.favorites)

        # Add tweet details to csv array
        if tweetInfo not in csvData:
            csvData.append(tweetInfo)

    # Tokenize tweets and mentions
    for i in tweetset:
        token = nltk.word_tokenize(i, language='english')
        for j in token:
            words.append(j.lower())

# Create copy of current words
cleanwords = words[:]

# Remove punctuation, stopwords and unnecessary terms
for i in words:
    if i in swords:
        cleanwords.remove(i)
    elif i in string.punctuation:
        cleanwords.remove(i)
    elif 'country' in i:
        cleanwords.remove(i)
    elif 'inn' in i:
        cleanwords.remove(i)
    elif 'www' in i:
        cleanwords.remove(i)
    elif '.' in i:
        cleanwords.remove(i)
    elif 'http' in i:
        cleanwords.remove(i)
    elif i == "I":
        cleanwords.remove(i)
    elif i == "…":
        cleanwords.remove(i)
    elif i == "...":
        cleanwords.remove(i)
    elif "’" in i:
        cleanwords.remove(i)
    elif "`" in i:
        cleanwords.remove(i)
    elif "/" in i:
        cleanwords.remove(i)
    elif i == "'s":
        cleanwords.remove(i)
    elif "—" in i:
        cleanwords.remove(i)
    elif "-" in i:
        cleanwords.remove(i)
    elif i == "''":
        cleanwords.remove(i)
    elif i == "``":
        cleanwords.remove(i)
    elif "'" in i:
        cleanwords.remove(i)
    elif i == "'m":
        cleanwords.remove(i)
    elif '“' in i:
        cleanwords.remove(i)
    elif '”' in i:
        cleanwords.remove(i)

# Create dict of frequencies
count = nltk.FreqDist(cleanwords)

# Plot graph of frequencies
graph = sorted(count.items(), key=operator.itemgetter(1))
key, val = zip(*graph)
plt.barh(key[len(key) - 30:], val[len(val) - 30:])
plt.plot()

# Create csv of all tweets
with open('countryinn_tweets.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()

# Create csv of frequency counts
with open('countryinn_counts.csv', 'w') as csvFile2:
    writer = csv.writer(csvFile2)
    writer.writerow(['word','count'])
    for row in graph:
        writer.writerow(row)
csvFile.close()

# Ending processes
print('Run Complete')
plt.savefig('countryinn.png')
plt.show()
