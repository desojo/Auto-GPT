import tweepy
global cfg
from config import Config

cfg = Config()

#authenticating to twitter
api = tweepy.Client(bearer_token=cfg.twitter_bearer_token,
                        access_token=cfg.twitter_access_token,
                        access_token_secret=cfg.twitter_access_token_secret,
                        consumer_key=cfg.twitter_api_key,
                        consumer_secret=cfg.twitter_api_key_secret)

def post_tweet(tweet):
    """Post a Tweet to the @AutoGPTweeter account using the Tweepy API"""
    api.create_tweet(text=tweet)




