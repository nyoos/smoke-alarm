from helpers.twitter_api_wrapper import send_message

welcome_text = "Thank you for following us! SmokeAlarm is a program that hopes to help you better recognise and spot early signs of burn out and excess stress through analysis of social media platforms. "
good_text = "Currently, your mood and stressors are trending neutral or positive! "
bad_text = "Currently, your mood and stressors are trending negative - do check out some of the resources linked below! "
end_text = "If you find yourself feeling burnt out, here are some resources that may help: \n https://www.healthline.com/health/mental-health/burnout-recovery\nhttps://www.forbes.com/sites/ashleystahl/2020/11/13/9-ways-to-recover-from-burnout-and-love-your-job-again/?sh=2e57a45124a5\nhttps://www.mindtools.com/pages/article/recovering-from-burnout.htm"
import getopt, sys
import json

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = ["u:l"]
long_options = ["userid=","lastpostid="]


arguments, values = getopt.getopt(argument_list, short_options, long_options)
user_id = values[0]
if values[1]==1:
  send_message(user_id,welcome_text + good_text + end_text)
else:
  send_message(user_id,welcome_text + bad_text + end_text)



