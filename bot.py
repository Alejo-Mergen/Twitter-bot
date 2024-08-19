import tweepy
from datetime import datetime
import schedule
import time
import tweepy.client
import os

from dotenv import load_dotenv, dotenv_values


config = dotenv_values(".env")

api_key = config["api_key"]
api_secret = config["api_secret"]
baerer_token = config["baerer_token"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

client = tweepy.Client(baerer_token, api_key, api_secret, access_token, access_token_secret)


def enviar_tweet():
    # Obtener la hora actual
    hora_actual = datetime.now().strftime("%H:%M")
    # Crear un tweet
    client.create_tweet(text = f'Tomar Agua a las {hora_actual}')
    print('Tweet enviado')

# Programar el tweet para que se envíe cada hora
schedule.every().hour.do(enviar_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)