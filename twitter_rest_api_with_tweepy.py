import os

import tweepy 

TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Authentication 
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# get a API client
api = tweepy.API(auth)

# get a timeline
public_tweets = api.home_timeline()

# print out username and tweet from response
for status in public_tweets:
    print('@' + status.user.screen_name, status.text)
