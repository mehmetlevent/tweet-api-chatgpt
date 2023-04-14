import tweepy
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


api_key = config.get("TwitterAPI", "ApiKey")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(AccessToken, AccessSecret)

api = tweepy.API(auth)
tweet = "bu ya chatgpt api den gelecek"
api.update_status(tweet)

print("tweet posted"+ tweet)