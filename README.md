# twitter-scrape
#### Introduction
Python program to scrape a sample of tweets associated with Margaritaville. 
This is part of a project in the University of Virginia McIntire School of Commerce. 

Results are used to conduct brand equity analysis about common words people think of 
when 'Margaritaville' is mentioned. 

#### Required Modules

1. got3: https://github.com/Jefferson-Henrique/GetOldTweets-python
    - For retrieving historical tweets
2. nltk
    - For tokenizing words and counting frequencies
3. nltk.corpus import stopwords
    - For removing stopwords (words that add no value to data)
4. string
    - For removing punctuation
5. time
    - For counting time taken for each data extraction
6. random
    - For getting random sampling of dates
6. matplotlib.pyplot
    - For plotting the frequency distributions
7. operator
    - For converting nltk dict into tuples
8. csv
    - For exporting data to csv
9. re
    - For extracting username from twitter permalink

#### Note
Program will create a new "tweets.csv" file within current directory