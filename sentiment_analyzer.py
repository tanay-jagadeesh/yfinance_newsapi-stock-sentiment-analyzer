import sqlite3
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from text_processor import remove_url, remove_special_characters, lowercase, remove_whitespace
from match_data import cleaned

# Connect to database
conn = sqlite3.connect('news.sentiment.db')

# Load articles
articles_df = pd.read_sql_query("SELECT * FROM articles", conn)


analyzer = SentimentIntensityAnalyzer()
articles_df['combined_scores'] = (articles_df['title'].fillna('') + ' ' + articles_df['description'].fillna('')).apply(cleaned)

def get_sentiments(txt):
    scores = analyzer.polarity_scores(txt)
    return scores 

articles_df['vader_sentiment'] = articles_df['combined_scores'].apply(get_sentiments)

print(f"Sentiment Scores: {articles_df['vader_sentiment']}")

articles_df['neg'] = articles_df['vader_sentiment'].apply(lambda x: x['neg'])

articles_df['neu'] = articles_df['vader_sentiment'].apply(lambda x: x['neu'])

articles_df['pos'] = articles_df['vader_sentiment'].apply(lambda x: x['pos'])

articles_df['compound'] = articles_df['vader_sentiment'].apply(lambda x: x['compound'])

print(articles_df[['title', 'neg', 'neu', 'pos', 'compound']].head())

def classify_sentiment(compound):
    if compound > 0.05:
        return "bullish"
    elif compound < -0.05:
        return "bearish"
    else:
        return "neutral"

articles_df['classify'] = articles_df['compound'].apply(classify_sentiment)

print(articles_df[['title', 'compound', 'classify']].head(10))

print(f"The average compound score: {articles_df['compound'].agg('mean')}")

total = len(articles_df['classify'])

print(f"The % bullish articles: {(articles_df['classify'] == "bullish").sum() / total}")

print(f"The % bearish articles: {(articles_df['classify'] == "bearish").sum() / total}")

print(f"The average compound score for each ticker: {articles_df.groupby('ticker')['compound'].mean()}")

print(f"The % neutral articles: {(articles_df['classify'] == "neutral").sum() / total}")

