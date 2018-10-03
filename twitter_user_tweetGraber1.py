# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:24:57 2018

@author: Moji
"""
from tweeter_credentials import *
import re
import tweepy
import csv
consumer_key=CONSUMER_KEY
consumer_secret= CONSUMER_SECRET
access_key= ACCESS_TOKEN
access_secret= ACCESS_TOKEN_SECRET



def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_key, access_secret)
   api = tweepy.API(auth)
   alltweets = []	
   new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended')
   #save most recent tweets
   alltweets.extend(new_tweets)
    
   #save the id of the oldest tweet less one
   oldest = alltweets[-1].id - 1
    
   #keep grabbing tweets until there are no tweets left to grab
   while len(new_tweets) > 0:
    print ("getting tweets before %s" % (oldest))
    	
    #all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, tweet_mode='extended')
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    	
    #update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    	
    print ("...%s tweets downloaded so far" % (len(alltweets)))
    cleaned_text = [re.sub(r'http[s]?:\/\/.*[\W]*', '', i.full_text, flags=re.MULTILINE) for i in alltweets] # remove urls
    cleaned_text = [re.sub(r'@[\w]*', '', i, flags=re.MULTILINE) for i in cleaned_text] # remove the @twitter mentions 
    cleaned_text = [re.sub(r'RT.*','', i, flags=re.MULTILINE) for i in cleaned_text] # delete the retweets
    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, tweet.created_at, cleaned_text[idx].encode("utf-8")] for idx,tweet in enumerate(alltweets)]
    
    #write the csv	
    with open('C:/Users/Moji/Documents/%s_tweets.csv' % screen_name, 'w') as f:
    	writer = csv.writer(f)
    	writer.writerow(["id","created_at","text"])
    	writer.writerows(outtweets)

get_all_tweets("realDonaldTrump")

new_tweets = api.user_timeline(screen_name = 'jemwilson84' ,count=200, tweet_mode='extended')
#user = api.get_user('jemwilson84')
new_tweets[4]
tweet_texts = [tweet.full_text for tweet in new_tweets]
print(user.screen_name)
print(user.followers_count)



