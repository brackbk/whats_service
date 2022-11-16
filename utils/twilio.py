# utils
import os
import sys
import json
from utils.config import Config
from twilio.rest import Client
# GCP

class Twilio:
    def __init__(
            self
        ):
        self.client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

    def sendSms(self, template, number):

        try:
            message = self.client.messages.create(
                            body=template,
                            from_=Config.TWILIO_FROM,
                            to=number
                        )

            return message.sid
        except Exception as e:
            print(e)
            raise Exception("Fail to send msg")

    def sendWhats(self, template, number):    
        try:
            message = self.client.messages.create(
                    body=template,
                    from_="whatsapp:" + Config.TWILIO_FROM,
                    to="whatsapp:" + number
                )
            print(message)
            return {
                'status':'success',
                'sid': message.sid
            }
        except Exception as e:
            print(e)
            raise Exception("Fail to send msg")


    def sendNotification(self, template, number):
        try:
            notification = self.client.notify.services(Config.TWILIO_NOTIFY_SID) \
            .notifications.create(
                to_binding='{"binding_type":"sms", "address":"'+number+'"}',
                body=template)
            
            return notification.sid
        except Exception as e:
            print(e)
            raise Exception("Fail to send msg")