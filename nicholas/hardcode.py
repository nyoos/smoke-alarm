import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

USER_ID = os.environ.get("USER_ID")

def twitter_auth_and_connect(bearer_token, url, params):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	response = requests.request("GET", url, headers=headers, params=params)
	if(response is None):
		print("no response")
	return response

def gettweets():

	response = twitter_auth_and_connect(BEARER_TOKEN, f"https://api.twitter.com/2/users/{USER_ID}/followers",None)
	print("these are my followers")
	print(response.json())

	print("")
	print("")
	
	for follower in response.json()['data']:

		params = {
			"max_results":100
		}

		follower_id = follower['id']

		print("These are the posts of follower with id", follower_id)

		user_timeline = twitter_auth_and_connect(BEARER_TOKEN, f"https://api.twitter.com/2/users/{follower_id}/tweets", params=params)

		for post in user_timeline.json()['data']:
			print(post['text'])

		
def getUserID(username):

	response = twitter_auth_and_connect(BEARER_TOKEN, f"https://api.twitter.com/2/users/by/username/{username}",None)

	print(response.json())

def main():
	
	getUserID("nicholas_is_dum")

	#gettweets()


if __name__ == "__main__":
	main()