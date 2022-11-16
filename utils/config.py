import os
from os import environ, path

class Config:

    #PubSub config
    TOPIC_PUB = os.getenv('TOPIC_PUB')
    PROJECT_ID = os.getenv('PROJECT_ID')

    #Slack config
    SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
    SLACK_DEFAULT_CHANNEL = os.getenv('SLACK_DEFAULT_CHANNEL')
    
    #twilio config
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_FROM = os.getenv('TWILIO_FROM') 

    