# utils
from services.whats import WhatsService
import json
def whats_service(event, context):
    try:

        whats = WhatsService(event)

        response = whats.send()
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(response)
        }
    except Exception as e:
        print(str(e))
        pass


if __name__ == "__main__":
    event = {
        "number": "+5545999052903",
        "template": "hola, {{1}} , {{2}} que está a  su cargo pidió permiso y necesita su Autorización, el motivo * {{3}} * alega que {{4}} el permiso corresponde  desde {{5}} hasta {{6}}"
    }
    print(whats_service(event, ""))



