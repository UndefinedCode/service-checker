#!/usr/bin/python3

import os
import requests
import logging
import time
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
MY_NUMBER = os.getenv('MY_NUMBER')
URL = os.getenv('URL')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
logging.basicConfig(
    filename='./log',
    filemode='a', 
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

if __name__ == "__main__":
    def status_check():
        response = requests.get(URL)

        if response.status_code == 200:
            logging.info('Все в порядке')
            time.sleep(60)
            status_check()
        else:
            logging.error('Сайт упал')
            client.messages.create(
                body='Сайт упал',
                from_=TWILIO_NUMBER,
                to=MY_NUMBER
            )

    status_check()

    

            