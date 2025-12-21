# News Sentiment Analyzer for Stock Mentions
# Day 1: Set up News API
import pandas as pd
from datetime import datetime, timedelta
import requests
import config


params = {
    "from": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
    "to": datetime.now().strftime("%Y-%m-%d")  
}

stocks_in_demand = ["AAPL", "GOOGL", "MSFT", "TSLA", "META", "NVDA", "AMZN", "JPM", "BAC", "GS", "V", "WMT", "JNJ", "UNH", "DIS"]

ticker_symbols = {
    "AAPL": "Apple",
    "GOOGL": "Google",
    "MSFT": "Microsoft",
    "TSLA": "Tesla",
    "META": "Meta OR Facebook",
    "NVDA": "Nvidia",
    "AMZN": "Amazon",
    "JPM": "JPMorgan OR JP Morgan",
    "BAC": "Bank of America",
    "GS": "Goldman Sachs",
    "V": "Visa",
    "WMT": "Walmart",
    "JNJ": "Johnson & Johnson",
    "UNH": "UnitedHealth OR United Health",
    "DIS": "Disney"
}

"""Extracts News from Api"""
def extract_news(response, key):
    for article in response.json()['articles']:
        data = {
            "ticker": key,
            "source": article['source'],
            "title": article['title'],
            "author": article['author'],
            "description": article['description'],
            "url": article['url'],
            "publishedAt": article['publishedAt'],
            "content": article['content']
        }
        article_list.append(data)

article_list = []
for key in ticker_symbols:
    response = requests.get(f"https://newsapi.org/v2/everything?q={ticker_symbols[key]}&pageSize=20&apiKey={config.API_KEY}", params = params)

    # Error Handling to see if it prints json
    try:
        response.raise_for_status()
        extract_news(response, key)
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            print(f"You have reached your rate limit for {key}")
        else:
            print(f"HTTP error for {key}: {e}")

df = pd.DataFrame(article_list)
df.to_csv('news_data.csv', index=False)