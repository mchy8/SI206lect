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

api_authorization = tweepy.API(auth)
# api_authorization.update_status(input("What photo would you like to tweet? "))

#or is it:
photo_path = "~/Desktop/creamcheese.jpg"
status = "#UMSI-206", "#Proj3"
api_authorization.update_with_media(photo_path, status=status)
# api_authorization.update_with_media(creamcheese.jpg["#UMSI-206", "#Proj3"])



# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")