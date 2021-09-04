import api.twitter_api_wrapper

user = api.twitter_api_wrapper.get_user_id("geminiminiz")
api.twitter_api_wrapper.send_message(user,"Hello world")