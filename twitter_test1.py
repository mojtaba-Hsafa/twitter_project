# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:45:16 2018

@author: Moji
"""

from tweeter_credentials import *

import tweepy

api = twitter.Api(consumer_key=CONSUMER_KEY,
  consumer_secret= CONSUMER_SECRET,
  access_token_key= ACCESS_TOKEN,
  access_token_secret= ACCESS_TOKEN_SECRET)

search = api.GetSearch("ISIS") # Replace happy with your search
for tweet in search:
    print(tweet.id, tweet.text)
