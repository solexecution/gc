import tweepy 
import creds # credentials for authorization

""""
using AppAuthHandler to go faster as we need read-only access to public information
"""
auth = tweepy.AppAuthHandler(creds.consumer_key,creds.consumer_secret) 
api = tweepy.API(auth)

# twitter_accounts = ['@get_chip','@monzo','@StarlingBank','@RevolutApp']


account_tweets = tweepy.Cursor(api.search, q='revolut'+'-filter:retweets').items(1000)

for tweet in account_tweets:
    print(tweet._json)

# for tweet in tweepy.Cursor(api.search, q='@get_chip'+'-filter:retweets').items(100):
