import tweepy
global cfg
from config import Config

cfg = Config()
tweetID = []
tweets = []
#authenticating to twitter
auth = tweepy.OAuth1UserHandler(cfg.twitter_api_key, cfg.twitter_api_key_secret,
                                cfg.twitter_access_token, cfg.twitter_access_token_secret)

api = tweepy.API(auth)

def post_tweet(tweet):
    """Post a Tweet to the @AutoGPTweeter account using the Tweepy API"""
    tweetID = api.update_status(status=tweet)
    return "Success! Tweet ID: " + str(tweetID.id)

def get_mentions():
    """Get the mentions to the @AutoGPTweeter account using the Tweepy API"""
    tweets = api.mentions_timeline(tweet_mode="extended")
    tweetList = []

    for tweet in tweets:
        tweetList.append("@" + tweet.user.screen_name + " Replied: " + tweet.full_text)

    return tweetList

