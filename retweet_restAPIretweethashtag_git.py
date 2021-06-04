#!/usr/bin/env python
# tweepy-bots/bots/retweet_restAPIretweethashtag_git.py

import tweepy
import logging
#from config import create_api
import json
import os
import time

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	
#searchQuery = '#sciencepolicy OR #STIP2021 OR #scipol OR #scienceadvice OR #sciencediplomacy OR #scidip OR #scicomm OR #aipolicy OR #netneutrality OR #Coviddiplomacy OR #vaccinediplomacy OR #techdiplomacy OR #techplomacy OR #ScienceTechnologyStudies OR #researchandinnovation OR  #scienceethics OR #datagovernance OR #biosecurity OR #innovationstudies OR #industryresearch OR #scienceandinnovation OR #emergingtechnologies OR #researchpolicy OR #spacepolicy OR #UNFCCC  -filter:retweets AND -filter:replies'
searchQuery = '#sciencepolicy OR #STIP2021 OR #scipol OR #scienceadvice OR #sciencediplomacy \
OR #scidip OR #scicomm OR #aipolicy OR #Coviddiplomacy OR #vaccinediplomacy \
OR #techdiplomacy OR #techplomacy OR #ScienceTechnologyStudies OR #researchandinnovation \
OR #biosecurity OR #innovationstudies OR #industryresearch OR #emergingtechnologies OR #UNFCCC OR STIP2020  -filter:retweets AND -filter:replies'

# central India geocode
geoCentral = '21.812672,80.183887,684mi' #Balaghat,MP to Kolkata, WB & Jamnagar, Gujarat
# South India geocode
geoSouth = '14.777141,77.305469,560mi' #Korakudu, AP to Mumbai & Nagercoil, TN
# NE India geocode
geoNE = '25.906067,93.286162,379mi ' #Krabi Anglong, Assam to Lunglei, Mizoram
# North India geocode
geoNTH = '34.155731,77.577378,420mi' #Leh to Shimla, HP . may also get signal from islambad,, Pakistan

# New Delhi geocode	- New Delhi to Amritsar radius 450 km
for tweet in tweepy.Cursor(api.search, q=searchQuery, geocode='28.618336,77.222019,280mi', lang='en', count=1000).items():
	try:
		tweet.retweet()
		print("Tweet retweet")
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)

# central India
for tweet in tweepy.Cursor(api.search, q=searchQuery, geocode=geoCentral, lang='en', count=1000).items():
	try:
		tweet.retweet()
		print("Tweet retweet")
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)

# Southern India
for tweet in tweepy.Cursor(api.search, q=searchQuery, geocode=geoSouth, lang='en', count=1000).items():
	try:
		tweet.retweet()
		print("Tweet retweet")
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)

# NE India		
for tweet in tweepy.Cursor(api.search, q=searchQuery, geocode=geoNE, lang='en', count=1000).items():
	try:
		tweet.retweet()
		print("Tweet retweet")
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)

# North of north India
for tweet in tweepy.Cursor(api.search, q=searchQuery, geocode=geoNTH, lang='en', count=1000).items():
	try:
		tweet.retweet()
		print("Tweet retweet")
		time.sleep(10)
	except tweepy.TweepError as e:
		print(e.reason)

