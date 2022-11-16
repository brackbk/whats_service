from utils.config import Config
from utils.twilio import Twilio
from domain.whats import Whats
from datetime import datetime
from pytz import timezone
import locale

locale.setlocale(locale.LC_ALL, "")

class WhatsService:
        
    def __init__(self, event):
        self.whatsDomain = Whats(event)
        self.whats = self.whatsDomain.data()
        self.twilio = Twilio()
        self.time_formated = datetime.now(timezone("America/Asuncion")).strftime("%H:%M")


    def send(self):
        try:
            number = self.whats['number']
            template = self.whats['template']
            print(f"Hora: {self.time_formated} - send to number {number}")
            return self.twilio.sendWhats(template, number)
        except Exception as e:
            print(e)
            raise Exception("Error to send to numbers")        
