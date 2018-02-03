#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, logging

with open("config.json") as json_data:
    config = json.load(json_data)

auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
auth.set_access_token(config['ACCESS_KEY'], config['ACCESS_SECRET'])
api = tweepy.API(auth)

logger = logging.getLogger("tweetbot")

posts = api.search("#bitcoin", rpp=100, page=2)

for post in posts:
    print ("Text:" + str(post.text) + "\n")
    print ("RT" + str(len(post.retweets())) + "\n")
