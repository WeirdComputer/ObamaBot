#!/usr/bin/python3

from datetime import datetime

import requests
import os

import random

import tweepy
import configparser


#Set custom cfg.ini FULL path here.

#customconfigpath = ''



config = configparser.ConfigParser()

# Comment out if using custom path

config.read( os.environ['HOME'] + "/.config/obamabot/cfg.ini")

# Uncomment to use custom path set above.
#config.read( customconfigpath )


# Check to see if the user configured the bot, fail if they have not.

enabled = config['Bot']['enabled']

if enabled.lower == true:
    print("Bot enabled")
else
    print("Bot disabled")
    exit()

now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

# Authenticate to Twitter

auth = tweepy.OAuthHandler(config['Auth']['CONSUMER_KEY'], config['Auth']['CONSUMER_SECRET'])
auth.set_access_token(config['Auth']['ACCESS_TOKEN'], config['Auth']['ACCESS_TOKEN_SECRET'])


# Create API object

api = tweepy.API(auth)


# Push list of configured links into an array split by comma

links = config['Links']['listname'].split(",")

# Uploads a random link using the target twitter handle as the status update.

filename = 'temp.jpg'
request = requests.get(random.choice(config['Links']['listname'].split(",")), stream=True)
if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)

    api.update_with_media(filename, status=config['Targets']['target1name'])

    os.remove(filename)

else:
    print("Can't tweet bro.")

