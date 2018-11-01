import got3
import nltk
from nltk.corpus import stopwords
import string
import time

# api = twitter.Api(consumer_key='t5vPzosVoa1gTEYDR4CeqXW4G',
#                   consumer_secret='u0lGoV9Q1WpPMQCNFvoxZijfdN6joXmFuBqAIXJKI2kDIrOPC8',
#                   access_token_key='1010518682202562560-4Y8YdB2KcIUyah1KhCzgAjd91jUaIm',
#                   access_token_secret='MIym8gUUdJuC7sdddqeeU77X3LhuHUm7RAspcymDZTx5y')


tweetCriteria = got3.manager.TweetCriteria()\
    .setQuerySearch("Margaritaville")\
    .setSince("2017-10-29")\
    .setUntil("2017-10-30")\
    # .setMaxTweets(100)

start = time.time()
tweet = got3.manager.TweetManager.getTweets(tweetCriteria)
end = time.time()

swords = stopwords.words('english')
words = []

for i in tweet:
    token = nltk.word_tokenize(i.text, language='english')
    for j in token:
        if '@' not in token:
            words += token

for i in range(len(words)):
    words[i] = words[i].lower()
    words[i] = words[i].lower()

cleanwords = words[:]

for i in words:
    if i in swords:
        cleanwords.remove(i)
    if i in string.punctuation:
        cleanwords.remove(i)
    if 'bit.ly' in i:
        cleanwords.remove(i)
    if '.com' in i:
        cleanwords.remove(i)
    if '.me' in i:
        cleanwords.remove(i)
    if ('http' or 'https') in i:
        cleanwords.remove(i)
    if 'margaritaville' in i:
        cleanwords.remove(i)
    if i == "I":
        cleanwords.remove(i)
    if i == "…":
        cleanwords.remove(i)
    if i == "...":
        cleanwords.remove(i)
    if i == "’":
        cleanwords.remove(i)
    if i == "`":
        cleanwords.remove(i)
    if i == "'s":
        cleanwords.remove(i)
    if i == "—":
        cleanwords.remove(i)
    if i == "''":
        cleanwords.remove(i)

count = nltk.FreqDist(cleanwords)

for key, val in count.items():
    print(str(key) + ' : ' + str(val))

print(end-start)

count.plot(20, title="Words associated with Margaritaville Tweets")