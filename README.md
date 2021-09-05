# Smoke Alarm

Smoke Alarm is a twitter bot that helps users track their mood and stress levels over time through emotion analysis of previous tweets.

Built with NodeJS and Python, hosted on heroku and MongoDB.

## Functionality

The bot periodically scans its followers list and adds new followers to a tracking list where new posts are analysed for emotion and stress levels. The actual tweets themselves are not stored on the backend. Periodically, the bot will check a user's history to check for any trends or warning signs of burnout (persistent feelings of stress or stress levels that trend higher over time). The bot then sends the users messages to warn them of such signals.

## Build Instructions

NodeJS dependencies can be installed with npm, and python dependencies can be installed using the requirements.txt file.

npm start to begin running.

Link to account: https://twitter.com/nyoos9
