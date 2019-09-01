import tweepy
import creds  # credentials for authorization
import json
import time

""""
using AppAuthHandler to go faster as we need read-only access to public information
"""
auth = tweepy.AppAuthHandler(creds.consumer_key, creds.consumer_secret)
api = tweepy.API(auth)

# ,'#get_chip','#monzo','#StarlingBank','#RevolutApp']
twitter_accounts = ['@get_chip', '@monzo', '@StarlingBank', '@RevolutApp']

#  https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html


def collect_account_tweets(account_iterable, multifile=True):
    tweet_collection = [tweet._json for tweet in account_iterable]
    if(multifile):
        with open(time.strftime("%H%M%S_%d%m%Y_")+'tweets_'+str(len(tweet_collection))+'.json', 'at') as f:
            json.dump(tweet_collection, f)
            f.close()
    else:
        with open('tweets.json', 'w') as f:
            json.dump(tweet_collection, f)
            f.close()


for account in twitter_accounts:
    account_tweets = tweepy.Cursor(api.search, q=account+'-filter:retweets').items(100)
    collect_account_tweets(account_tweets, multifile=True)
