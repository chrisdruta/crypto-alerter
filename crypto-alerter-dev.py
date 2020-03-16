#!/usr/bin/env python3
import os

import requests
from dataclasses import dataclass

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CHANGE_PERCENT_THRESHOLD = 7
COINS_TO_CHECK = ['ethereum']

def main():
    for coin in COINS_TO_CHECK:
        p = Ping(coin)
        print(p)
        if p.price_change_percentage_24h > CHANGE_PERCENT_THRESHOLD:
            send_email('magic internet money update!!', str(p))

@dataclass
class Ping:
    def __init__(self, coin:str, **kwargs):
        r = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}')
        for kw, v in r.json()[0].items():
            if kw in self.__dataclass_fields__.keys():
                self.__setattr__(kw, v)

    symbol: str
    last_updated: str

    price_change_percentage_24h: float
    price_change_24h: float

    current_price: float
    high_24h: float
    low_24h: float

def send_email(subject:str, body: str) -> None:
    login_address = os.getenv('GMAIL_USER')
    secret = os.getenv('GMAIL_PASS')
    to_address = os.getenv('ALERT_PHONE_NUMBER_EMAIL')

    if any(map(lambda e: e == None, [login_address, secret, to_address])):
        print('missing required environment variables')
        exit(1)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login_address, secret)

    msg = MIMEMultipart()

    msg['From'] = login_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server.sendmail(login_address, to_address, msg.as_string())
    server.quit()

if __name__ == '__main__':
    main()
