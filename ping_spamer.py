import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests
import logging
import time

logging.basicConfig(format="%(levelname)s %(asctime)s %(message)s", level=logging.INFO)

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_PHONE_NUMBER = os.getenv('FROM_PHONE_NUMBER')
TO_PHONE_NUMBER = os.getenv('TO_PHONE_NUMBER')
URL = os.getenv('URL')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(message_text):
    try:
        message = client.messages.create(
            body=message_text,
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
        logging.info(f'Сообщение {message_text} отправлено')
    except Exception:
        logging.info(f'Сообщение не отправлено')


response = requests.get(URL)
print(response.status_code)
