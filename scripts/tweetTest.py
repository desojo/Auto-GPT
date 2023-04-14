import tweepy
import json
global cfg
from config import Config

cfg = Config()

def post_tweet(tweet):
    """Post a Tweet to the @AutoGPTweeter account using the Tweepy API"""
    # Get the twitter API keys from the config file
    #auth = tweepy.OAuthHandler(
    #    cfg.twitter_api_key, cfg.twitter_api_key_secret,
    #    cfg.twitter_access_token, cfg.twitter_access_token_secret)

    client = tweepy.Client(cfg.twitter_bearer_token)

    client = tweepy.Client(
        cfg.twitter_api_key, cfg.twitter_api_key_secret,
        cfg.twitter_access_token, cfg.twitter_access_token_secret)

    print(cfg.twitter_api_key)
    print(cfg.twitter_api_key_secret)
    print(cfg.twitter_bearer_token)
    print(cfg.twitter_access_token)
    print(cfg.twitter_access_token_secret)

    response = client.create_tweet(text=tweet)

    print(response)

tweet = str(input("Enter in the tweet you want to post: "))

post_tweet(tweet)


