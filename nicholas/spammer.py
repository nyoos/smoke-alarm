import requests
import os
import json
from dotenv import load_dotenv

from requests_oauthlib import OAuth1Session, OAuth1


load_dotenv()


CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

USER_ID = os.environ.get("USER_ID")


def buildOAuth():
	
	request_token_url = "https://api.twitter.com/oauth/request_token"
	
	print("CONSUMER_KEY", CONSUMER_KEY)
	print("CONSUMER_SECRET", CONSUMER_SECRET)
	
	oauth = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)

	try:
		fetch_response = oauth.fetch_request_token(request_token_url)
	except ValueError:
		print(
			"There may have been an issue with the consumer_key or consumer_secret you entered."
		)
	
		
	resource_owner_key = fetch_response.get("oauth_token")
	resource_owner_secret = fetch_response.get("oauth_token_secret")
	print("Got OAuth token: %s" % resource_owner_key)

	# Get authorization
	base_authorization_url = "https://api.twitter.com/oauth/authorize"
	authorization_url = oauth.authorization_url(base_authorization_url)
	print("Please go here and authorize: %s" % authorization_url)
	verifier = input("Paste the PIN here: ")

	# Get the access token
	access_token_url = "https://api.twitter.com/oauth/access_token"
	oauth = OAuth1Session(
		CONSUMER_KEY,
		client_secret=CONSUMER_SECRET,
		resource_owner_key=resource_owner_key,
		resource_owner_secret=resource_owner_secret,
		verifier=verifier,
	)
	oauth_tokens = oauth.fetch_access_token(access_token_url)


	access_token = oauth_tokens["oauth_token"]
	access_token_secret = oauth_tokens["oauth_token_secret"]

	# Make the request
	oauth = OAuth1Session(
		CONSUMER_KEY,
		client_secret=CONSUMER_SECRET,
		resource_owner_key=access_token,
		resource_owner_secret=access_token_secret,
	)

	return oauth

def twitter_auth_and_connect(reqtype, bearer_token, url, params):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	response = requests.request(reqtype, url, headers=headers, params=params)
	if(response is None):
		print("no response")
	return response


def sendmessage(recipient_id):
	
	oauth = buildOAuth()	

	for i in range(10):
		mystring = "Post number " + str(i)
		
		headers = {
			"Content-Type":"application/json"
		}

		params = {"event": {"type": "message_create", "message_create": {"target": {"recipient_id": recipient_id}, "message_data": {"text": "Hello World!"}}}}

		#response.requests.post(url=f"https://api.twitter.com/1.1/statuses/update.json",params=params, oauth=oauth)
		response = oauth.post(f"https://api.twitter.com/1.1/direct_messages/events/new.json",headers=headers,data=json.dumps(params))
		#response = twitter_auth_and_connect("POST", BEARER_TOKEN, f"https://api.twitter.com/1.1/statuses/update.json",params=params)

		print(response.json())


def spam():

	#Makes a tweet.
	
	oauth = buildOAuth()

	for i in range(10):
		mystring = "Post number " + str(i)
		
		headers = {
			"Content-Type":"application/json"
		}

		#params = {"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "geminiminiz"}, "message_data": {"text": "Hello World!"}}}}
		#response.requests.post(url=f"https://api.twitter.com/1.1/statuses/update.json",params=params, oauth=oauth)


def main():
	sendmessage('1434024005497810946')

if __name__ == "__main__":
	main()