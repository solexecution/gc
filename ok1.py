import tweepy
import creds  # credentials for authorization
import json
import time
import pymongo
from pymongo import MongoClient
import sqlite3

""""
using AppAuthHandler to go faster as we need read-only access to public information
#  https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
"""
auth = tweepy.AppAuthHandler(creds.consumer_key, creds.consumer_secret)
api = tweepy.API(auth)

twitter_accounts = ['@XDDesign_']  # '@get_chip',#@monzo', '@StarlingBank', '@RevolutApp'

client = pymongo.MongoClient('mongodb+srv://'+creds.mongodb_user+':'+creds.mongodb_pwd+'@withlove-dwasi.mongodb.net/test?retryWrites=true&w=majority')
db = client.ibtweets
tweets = db.tweets
tweets.create_index([('created_at', pymongo.DESCENDING)])

for account in twitter_accounts:
    account_tweets = tweepy.Cursor(api.search, q=account, include_rts=0, tweet_mode='extended', result_type='recent').items(500)

    for tweet in account_tweets:
        tweets.insert_one(tweet._json)

print(tweets.find_one())