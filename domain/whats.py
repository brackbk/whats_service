from utils.config import Config
import json

class Whats():
    
    def __init__(self, event):
        # print(event)
        # self.payload = json.loads(event["body"])
        self.payload = event
    def data(self):

        result = {
            "template": self.payload["template"],
            "number": self.payload["number"].replace(" ", ""),
        }
        return result

        