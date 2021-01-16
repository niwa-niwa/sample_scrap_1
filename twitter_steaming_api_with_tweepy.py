import os
import tweepy


TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


def main():

    # Authentication 
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    # get stream object
    stream = tweepy.Stream(auth, MyStreamListener())

    # receive sampleing stream
    stream.sample(languages=['ja'])


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status: tweepy.Status):
        # the method is called when received tweet
        print('@' + status.author.screen_name, status.text)


if __name__ == '__main__':
    main()
