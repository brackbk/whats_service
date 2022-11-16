import os
from slack import WebClient
from slack.errors import SlackApiError
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class SlackNotification(Notification):
    def __init__(self, SLACK_API_TOKEN, SLACK_DEFAULT_CHANNEL):
        
        self.client = WebClient(token=SLACK_API_TOKEN)
        self.channel = SLACK_DEFAULT_CHANNEL
        
    def send(self, message):
        try:
            response = self.client.chat_postMessage(
                channel=self.channel,
                text=message
            )
            response["message"]["text"] == message

        except SlackApiError as e:
            print(e.response["error"])
