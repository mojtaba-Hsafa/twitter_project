# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:19:14 2018

@author: Moji
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:03:51 2018

@author: Moji
"""


#from timeline_REST_tweet_graber import *
from tweepy import Stream
from tweepy.streaming import StreamListener
import os
import csv
import sys
import sqlite3

#create sql table
conn = sqlite3.connect('twitter_one6.db')
c = conn.cursor()
c.execute('''CREATE TABLE tweets
    (date text,
    user text,
    tweet text)''')
conn.commit()
conn.close()

# open connection
conn = sqlite3.connect('twitter_one6.db')
c = conn.cursor()
class TweetListener(StreamListener):
    def __init__(self):
        super(TweetListener, self).__init__()
        self.file_index = 1
        
    def on_status(self, status):
        
        
        #tweets_file = 'C:/Users/Moji/Desktop/Raw_tweets{}.csv'.format(self.file_index)
        try:
            c.execute("INSERT INTO tweets (date, user, tweet) VALUES(?, ?,?)", 
                      (status.user.created_at,status.user.screen_name, status.text))
            conn.commit()
            
            
                #tweets_file = 'C:/Users/Moji/Desktop/Raw_tweets{}.csv'.format(self.file_index)
            
            return True
        except BaseException as e:
            print("failed in writting part!")
            print("Error on_data: %s" % str(e))
            conn.close()
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
'''
description = status.user.description
loc = status.user.location
text = status.text
coords = status.coordinates
name = status.user.screen_name
user_created = status.user.created_at
followers = status.user.followers_count
id_str = status.id_str
created = status.created_at

dabiq
caliphate or khilafah
Rumiyah

al-Sham

salafi
rahimahullah
hijrah

wajib aini

mubahala or mubahalah

hikmah

kafir of kuffar

Anwar al Awlaki 

Abu Bakr al-Baghdadi

sharia 

Mohammed Emwazi or Jihadi John

istitāba

mumāthila

istirāḥatal-mujāhidīn or mujtahidūn
Sally Jones or the White Widow

umma

ḥudūd
zakāt

bay'a or mubāyi’īn

Ayn al-Islām
'''
