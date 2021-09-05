from helpers.twitter_api_wrapper import get_followers
import json

followers = get_followers()
follower_ids = [int(datapoint["id"]) for datapoint in followers]
print(json.dumps(follower_ids))

# print(get_followers())