import sqlite3
import pandas as pd
from sklearn.preprocessing import StandardScaler

print("Loading data...")

# Load articles from database
conn = sqlite3.connect('news.sentiment.db')
articles_df = pd.read_sql_query("SELECT * FROM articles", conn)
conn.close()

# Load daily stats (already has price data and article counts)
daily_stats = pd.read_csv('daily_stats.csv')
