import requests
import os
import json
from dotenv import load_dotenv
import twitter


load_dotenv()

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")
TWITTER_USER_ID = os.environ.get("TWITTER_USER_ID")

def twitter_get(bearer_token, url, params):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	response = requests.request("GET", url, headers=headers, params=params)
	return response

def twitter_post(bearer_token, url, params):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	response = requests.request("POST", url, headers=headers, params=params)
	return response

def get_followers():

	response = twitter_get(TWITTER_BEARER_TOKEN, f"https://api.twitter.com/2/users/{TWITTER_USER_ID}/followers",None)
	return response.json()["data"]


def get_tweets(user_id):
	params = {
		"max_results":100,
		"tweet.fields":"created_at"
	}
	user_timeline = twitter_get(TWITTER_BEARER_TOKEN, f"https://api.twitter.com/2/users/{user_id}/tweets", params=params)
	return user_timeline.json()["data"]

def get_time_limited_tweets(user_id,time):
	params = {
		"max_results":100,
		"start_time":time,
		"tweet.fields":"created_at"
	}
	user_timeline = twitter_get(TWITTER_BEARER_TOKEN, f"https://api.twitter.com/2/users/{user_id}/tweets", params=params)
	if user_timeline.json()['meta']['result_count'] == 0:
		return []
	return user_timeline.json()["data"]

def get_user_id(username):

	response = twitter_get(TWITTER_BEARER_TOKEN, f"https://api.twitter.com/2/users/by/username/{username}",None)

	return(response.json()["data"]["id"])

def send_message(user,message):

	api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
	consumer_secret=TWITTER_CONSUMER_SECRET,
	access_token_key=TWITTER_ACCESS_TOKEN,
	access_token_secret=TWITTER_ACCESS_SECRET)
	status = api.PostDirectMessage(message,user)
	return status
