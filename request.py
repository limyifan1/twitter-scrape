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
# Create random list of 100 dates to search in past 10 years
for i in range(0, 5):
    year = random.randrange(2008, 2018)
    month = random.randrange(1, 13)
    day = random.randrange(1, 30)
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    dates.append(str(year) + "-" + str(month) + "-" + str(day))

csvData = [["Date", "Text", "Username", "Id", "Permalink", "Retweets", "Favorites"]]
words = []
counter = 0

for date in dates:
    tweetCriteria = got3.manager.TweetCriteria() \
        .setUntil(date) \
        .setQuerySearch("margaritaville") \
        .setMaxTweets(10) \
        .setTopTweets(True)

    start = time.time()
    tweet = got3.manager.TweetManager.getTweets(tweetCriteria)
    end = time.time()
    counter += 1
    print(str(counter), end - start)

    swords = stopwords.words('english')

    tweetset = set()

    for i in tweet:
        # print(i.__dict__)
        tweetInfo = []
        tweetset.add(i.text)
        tweetInfo.append(i.date)
        tweetInfo.append(i.text)

        username = re.search('https://twitter\.com/(.*)/status', i.permalink)
        username = username.group(1)
        tweetInfo.append(username)

        tweetInfo.append(i.id)
        tweetInfo.append(i.permalink)
        tweetInfo.append(i.retweets)
        tweetInfo.append(i.favorites)

        csvData.append(tweetInfo)

    tweet = tweetset

    for i in tweet:
        token = nltk.word_tokenize(i, language='english')
        if '@' not in token:
            for j in token:
                words.append(j.lower())

cleanwords = words[:]

for i in words:
    if i in swords:
        cleanwords.remove(i)
    elif i in string.punctuation:
        cleanwords.remove(i)
    elif 'margaritaville' in i:
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
    elif i == "—":
        cleanwords.remove(i)
    elif i == "''":
        cleanwords.remove(i)
    elif i == "``":
        cleanwords.remove(i)
    elif "'" in i:
        cleanwords.remove(i)
    elif i == "'m":
        cleanwords.remove(i)

count = nltk.FreqDist(cleanwords)

# for key, val in count.items():
#     print(str(key) + ' : ' + str(val))

graph = sorted(count.items(), key=operator.itemgetter(1))
key, val = zip(*graph)
plt.barh(key[len(key) - 20:], val[len(val) - 20:])
plt.plot()

with open('tweets.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()

with open('count.csv', 'w') as csvFile2:
    writer = csv.writer(csvFile2)
    writer.writerow(['word','count'])
    for row in graph:
        writer.writerow(row)
csvFile.close()

print('Run Complete')
plt.show()
