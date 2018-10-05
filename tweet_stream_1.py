# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:32:32 2018

@author: Moji
"""

from tweepy import Stream
from tweepy.streaming import StreamListener

class TweetListener(StreamListener):
    
    
    def on_status(self, status):
        
        print(status)
        return True
    def on_error(self,status):
        print(status)
        return True

python_stream_listener = TweetListener()
tweeter_gate= Tweepy_interface_creator()
auth =tweeter_gate.get_twitter_auth()
python_stream = Stream( auth , listener=python_stream_listener )

python_stream.filter(track=['python'])