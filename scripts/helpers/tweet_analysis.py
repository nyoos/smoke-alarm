import requests
from dotenv import load_dotenv
import os
load_dotenv()

HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")

def analyse_tweets(tweets):

  def clean_data(data):
    token_to_label = {"LABEL_0": "anger", "LABEL_1":"joy","LABEL_2":"optimism","LABEL_3":"sadness"}
    report = {"anger":0,"joy":0,"optimism":0,"sadness":0}
    for datapoint in data[0]:
      report[token_to_label[datapoint['label']]] = datapoint["score"]
    return report
    
  # def generate_report(data):
  #   length = len(data)
  #   report = {"anger":0,"joy":0,"optimism":0,"sadness":0}
  #   for datapoint in data:
  #     for label in datapoint:
  #       report[label['label']] += label['score']
  #   for key in report.keys():
  #     report[key] /= length
  #   return report

  

  API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion"
  headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

  payload = {
    "inputs": tweets,
    "options":{"wait_for_model":True}}

  response = requests.post(API_URL, headers=headers, json=payload)
  output = response.json()
  return clean_data(output)

def analyse_trend(history,thresholds):
  ## thresholds = {continuous_decrease,frequency}
  number_of_weeks_with_decrease = 0
  for week in range(1,len(history)):
    if history[week]['anger'] + history[week]['sadness'] - history[week-1]['anger'] - history[week-1]['sadness'] > thresholds['continuous_decrease']:
      number_of_weeks_with_decrease += 1

  return number_of_weeks_with_decrease >= thresholds['frequency']


def analyse_average(history,thresholds):
  ##thresholds = {average}
  average = sum([week['anger']+week['sadness'] for week in history])/len(history)
  return average > thresholds['average']