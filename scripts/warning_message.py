from helpers.twitter_api_wrapper import send_message

warning_text = "Hi, we've noticed an increase in stress and negative feelings in your recent tweets and would just like to check if you were doing fine! Remember that it's always okay to take a break to prevent yourself from burning out before it's too late! Have a quick breather before you return to work. Here are some tips to help you spot burnout and strategies to help you reset if necessary:\n https://www.healthline.com/health/mental-health/burnout-recovery\nhttps://www.forbes.com/sites/ashleystahl/2020/11/13/9-ways-to-recover-from-burnout-and-love-your-job-again/?sh=2e57a45124a5\nhttps://www.mindtools.com/pages/article/recovering-from-burnout.htm"
import getopt, sys
import json

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = ["u:l"]
long_options = ["userid=","lastpostid="]


arguments, values = getopt.getopt(argument_list, short_options, long_options)
user_id = values[0]
send_message(user_id,warning_text)



