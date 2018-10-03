# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:36:23 2018

@author: Moji
"""

import os 
import sys 
from tweepy import API 
from tweepy import OAuthHandler 
class Tweepy_interface_creator(): 
    def __init__(self,):
        pass
    def get_twitter_auth(self,): 
      """Setup Twitter authentication. 
     
      Return: tweepy.OAuthHandler object 
      """ 
      try: 
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN'] 
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
      except KeyError: 
        sys.stderr.write("TWITTER_* environment variables not set\n") 
        sys.exit(1) 
      auth = OAuthHandler(consumer_key, consumer_secret) 
      auth.set_access_token(access_token, access_secret) 
      return auth 
     
    def get_twitter_client(self,): 
      """Setup Twitter API client. 
     
      Return: tweepy.API object 
      """ 
      auth = self.get_twitter_auth() 
      client = API(auth) 
      return client 

from tweepy import Cursor 
import json
class REST_twitter_user():
    
    
    def __init__(self, twitter_gateway, name, tweet_num ):
        self.twitter_gate = twitter_gateway
        self.client = twitter_gate.get_twitter_client()
        self.user = name
        self.tweet_num = tweet_num
    def get_user_tweets(self,):
        tweet_objects=[]
        for status in Cursor(self.client.user_timeline, id=self.user, tweet_mode='extended').items(self.tweet_num): 
            tweet_objects.append(status)
        return [tweet.full_text for tweet in tweet_objects]
if __name__ == '__main__': 
    twitter_gate = Tweepy_interface_creator()
    trump_tweets = REST_twitter_user(twitter_gate,'RealDonaldTrump',1000)
    trump_text = trump_tweets.get_user_tweets()
    
    
    client = twitter_gate.get_twitter_client() 
    new_tweets = client.user_timeline(screen_name = 'RealDonaldTrump' ,count=200, tweet_mode='extended')
'''  
  tweets = [tweet.full_text for tweet in new_tweets]
  for page in Cursor(client.user_timeline(screen_name = 'RealDonaldTrump' ,count=200)).pages(3): 
    n_tweets= [status.text for status in page]
'''        