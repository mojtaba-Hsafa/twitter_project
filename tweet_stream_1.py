# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:32:32 2018

@author: Moji
"""
from timeline_REST_tweet_graber import *
from tweepy import Stream
from tweepy.streaming import StreamListener
import os
import json
import pandas as pd
class TweetListener(StreamListener):
    def __init__(self):
        super(TweetListener, self).__init__()
        self.file_index = 0
        
    def on_status(self, status):
        
        
        tweets_file = 'C:/Users/Moji/Desktop/Raw_tweets{}.txt'.format(self.file_index)
        try:
            
            with open(tweets_file, 'a',encoding="utf-8") as f:
                f.write(str(status))
                print(status.text)
                f.write('\n')
                
                return True
            '''
            while os.stat(tweets_file).st_size > 2**6:
                self.file_index += 1 
                tweets_file = 'C:/Users/Moji/Desktop/Raw_tweets{}.json'.format(self.file_index)
            '''
        except BaseException as e:
            print("failed in writting part!")
            print("Error on_data: %s" % str(e))
        
            return True
    def on_error(self,status):
        print(status)
        if status ==420:
            return False
        return True

python_stream_listener = TweetListener()
tweeter_gate= Tweepy_interface_creator()
auth =tweeter_gate.get_twitter_auth()
python_stream = Stream( auth , listener=python_stream_listener )

python_stream.filter(track=['ISIS'])
description = status.user.description
loc = status.user.location
text = status.text
coords = status.coordinates
name = status.user.screen_name
user_created = status.user.created_at
followers = status.user.followers_count
id_str = status.id_str
created = status.created_at