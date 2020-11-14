import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests
import logging
import time

logging.basicConfig(format="%(levelname)s %(asctime)s %(message)s", level=logging.INFO, filename='ping_spamer.log')

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_PHONE_NUMBER = os.getenv('FROM_PHONE_NUMBER')
TO_PHONE_NUMBER = os.getenv('TO_PHONE_NUMBER')
URL = os.getenv('URL')
SLEEP_TIME = 60

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(message_text):
    try:
        message = client.messages.create(
            body=message_text,
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
        logging.info(f'Message {message_text} sent')
    except Exception:
        logging.info("Message wasn't send")

count = 1
while count <= 20:
    response = requests.get(URL)
    status = response.status_code

    if status == 200:
        logging.info(f'Site {URL} is online')
    else:
        logging.info(f'{URL} gave error: {status} - send sms')
        send_sms(f'Site {URL} gave error: {status}')

    time.sleep(SLEEP_TIME)
    count += 1

