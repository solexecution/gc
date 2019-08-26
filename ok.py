import tweepy 
import creds # credentials for authorization
import json
import time

""""
using AppAuthHandler to go faster as we need read-only access to public information
"""
auth = tweepy.AppAuthHandler(creds.consumer_key,creds.consumer_secret) 
api = tweepy.API(auth)

# twitter_accounts = ['@get_chip','@monzo','@StarlingBank','@RevolutApp']

account_tweets = tweepy.Cursor(api.search, q='revolut'+'-filter:retweets').items(10)

tweet_collection = [tweet.id for tweet in account_tweets]

cnt = len(tweet_collection)

with open('tweets_'+str(cnt)+time.strftime("_%d%m%Y-%H%M%S_")+'.json', 'at') as f:
   json.dump(tweet_collection, f)
   f.close()
