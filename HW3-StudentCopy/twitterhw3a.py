# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.
import tweepy
from subprocess import call 
from datetime import datetime
#pulled a lot of this from the twitter code folder

access_token = "708355214034780162-Gbm6kBy0GDkPcy1ZzqogyJDeWy8o31R"
access_token_secret = "dk8PEiykjkqhaNQaU4gvXoJrDSvU8udCffqSrYQb6GTxs"
consumer_key = "QayiLxKVV5uwBOGnHvvCcDkCj"
consumer_secret = "BEkJOoTxvLzgxbJcjqY3wpxntSbrEyeH9S5378sxTTo3glKCZQ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
#setting variables

api_authorization = tweepy.API(auth)
#setting variable

status = "#UMSI206 #Proj3"
api_authorization.update_with_media("creamcheese.jpg", status=status)
#this allows it to update with both the picture and the hashtags
