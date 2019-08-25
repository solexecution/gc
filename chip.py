import pandas as pd
import tweepy

twitter_accounts = ['@get_chip', '@monzo', '@StarlingBank', '@RevolutApp']

print(twitter_accounts)

consumer_key = 'qLSVDZMb4XDKytE26DuApbNok'
consumer_secret = 'WJpcfIVv9Iu5nAa5A3fSx1bZdp34mlmmL7KShz1Jj81xK5mofM'
access_token = '859383719236444161-xdreob4U9B9JkpRR18q7htmKbKSIMI6'
access_token_secret = 'LpGtMOwdojIaDia391ydWoVBz34FLUlfpOTcBhpyPxR6M'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q=twitter_accounts).items(5)

# Collect a list of tweets
[tweet.text for tweet in tweets]
