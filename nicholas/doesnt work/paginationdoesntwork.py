		# while(True):
		# 	try:
		# 		nexttoken = user_timeline.json()['meta']['next_token']
		# 		print(nexttoken)
		# 		newparams = {
		# 			"max_results":100,
		# 			"pagination_token":nexttoken
		# 		}
		# 		user_timeline = twitter_auth_and_connect(BEARER_TOKEN, f"https://api.twitter.com/2/users/{follower_id}/tweets", params=params)
		# 		print(user_timeline.json()['meta'])
		# 	except:
		# 		break