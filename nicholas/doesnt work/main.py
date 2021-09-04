import tweepy

API_KEY = "l8LUltbto9uKe4u1pggMmQpen"
API_SECRET = "SO5Uwck2BTTIsrrkomBoKbQcZS98Ipij4J8zP2BEnfMzumRQkf"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIRtTQEAAAAAFJySukeQTn1VcZHgmsMufnDMtjI%3DjPW3aUX6YMIdoOF5ghPknCkheiKP1UcXH2mK0k32G895idHaFU"

ACCESS_TOKEN = "1431825305430212611-bpw5IoFIai4JfXaPPPDWCwCES7SMVM"
ACCESS_SECRET = "ko79OhGfZgjg6hYqjz7DYYPwUd8EOBLbtgJAPd5JPq1jA"



# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#api.update_status(":(((( sad")

timeline = api.home_timeline()

followers = api.followers()

for follower in followers:
	print("===========")
	print("These are the tweets for follower number")
	print(follower.id)

	user_tweets = api.user_timeline(user_id = follower.id)
	print("")

	for tweet in user_tweets:
		print(tweet.text)


# for tweet in timeline:
# 	print(f"{tweet.user.name} said {tweet.text}")

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")