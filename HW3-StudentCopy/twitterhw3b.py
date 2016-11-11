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
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('cheese')

reeses  = [tweet.text for tweet in public_tweets]
#this is pulling the text of the tweets collected

uprint(reeses)
#this helps with char code issues/unicode

subjectivity_accum = 0
polarity_accum = 0
#setting them both to zero so can accumulate 

for tweetz in reeses: 
	snicker = TextBlob(tweetz)
	subjectivity_accum += snicker.subjectivity
	polarity_accum += snicker.polarity


print("Average subjectivity is " + str(subjectivity_accum/len(reeses)))
#dividing the accumulator by the length
print("Average polarity is "+ str(polarity_accum/len(reeses)))
#dividing the accumulator by the length
