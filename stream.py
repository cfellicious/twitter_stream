import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import os
import sys
import time
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import OAuthHandler
 
consumer_key = 'ga6B4EsKcIGSpPUrfhmNS6ONW'
consumer_secret = 'rbzwVzR3ErRMASlsIBI6V4nhXF8yUq8Gd6rzHoXknUqjoLK3eI'
access_token = '782534371702079488-QQakHfKJKzmHvQVxO4Pm4K9DJraTPqT'
access_secret = 'nYUffFmsL6n15r1k10vSe1oxyOIABGluB00GtwMcw15ft'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Create the output file name with the date and month as the name.
# This will be easy to segregate the files by date

output_file_format = ".json"
curr_date = time.strftime("%d/%m/%Y")
output_file_name = "".join([curr_date[:2], curr_date[3:5], output_file_format])
print ("Output will be written to ", output_file_name)
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(output_file_name, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)	
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#AQuietPlace'])
