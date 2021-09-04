##Given a username, finds either the last 100 posts or up until the given post ID.
## Expects two arguments in the form of user id then last_post_id (optional)

from helpers.twitter_api_wrapper import get_tweets,get_time_limited_tweets
from helpers.tweet_analysis import analyse_tweets
import getopt, sys
import json

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = ["u:l"]
long_options = ["userid=","lastpostid="]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
    user_id = values[0]
    if len(values) > 1:
      last_check = values[1]
      tweets = get_time_limited_tweets(user_id,last_check)
      for tweet in tweets:
        tweet['score'] = analyse_tweets(tweet['text'])
      print(json.dumps(tweets))
    else:
      tweets = get_tweets(user_id)
      for tweet in tweets:
        tweet['score'] = analyse_tweets(tweet['text'])
      print(json.dumps(tweets))

except getopt.error as err:
    # Output error, and return with an error code
    print(str(err))
    sys.exit(2)