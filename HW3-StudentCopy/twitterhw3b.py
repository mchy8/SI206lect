# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# Unique code from Twitter
access_token = "708355214034780162-Gbm6kBy0GDkPcy1ZzqogyJDeWy8o31R"
access_token_secret = "dk8PEiykjkqhaNQaU4gvXoJrDSvU8udCffqSrYQb6GTxs"
consumer_key = "QayiLxKVV5uwBOGnHvvCcDkCj"
consumer_secret = "BEkJOoTxvLzgxbJcjqY3wpxntSbrEyeH9S5378sxTTo3glKCZQ"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('cheese')

reeses  = [tweet.text for tweet in public_tweets]

uprint(reeses)

# for tweet in public_tweets:
# 	print(tweet.text)

subjectivity_accum = 0
polarity_accum = 0

for tweetz in reeses: 
	snicker = TextBlob(tweetz)
	subjectivity_accum += snicker.subjectivity
	polarity_accum += snicker.polarity


print("Average subjectivity is " + str(subjectivity_accum/len(reeses)))
print("Average polarity is "+ str(polarity_accum/len(reeses)))
