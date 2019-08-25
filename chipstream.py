from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import creds

class StdOutLinstener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self,status):
        print(status)

if __name__ == "__main__":

    listener = StdOutLinstener()
    auth = OAuthHandler(creds.consumer_key, creds.consumer_secret)
    auth.set_access_token(creds.access_token,creds.access_token_secret)

    stream = Stream(auth, listener)

    stream.filter(track=['amazonia','notredame'])