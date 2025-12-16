# Twitter Sentiment Analyzer for Stock Mentions
# Day 1-2: Set up Twitter scraping

import praw
import pandas as pd
from datetime import datetime
import tweepy
import config

client = tweepy.Client(bearer_token = config.BEARER_TOKEN)

def search_tweets():
    response = client.search_recent_tweets(query = "$AAPL OR $TSLA OR $GOOGL", max_results = 10)
