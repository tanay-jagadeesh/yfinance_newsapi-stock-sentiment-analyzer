import pandas as pd
import sqlite3
import yfinance as yf
from news_headline_scraper import ticker_symbols 

conn = sqlite3.connect('stock_value.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS stock_prices (
    ticker TEXT,
    date TEXT,
    open REAL,
    close REAL,
    high REAL,
    low REAL,
    volume INTEGER,
    price_change_pct REAL
          )      
""")

start_date = '2025-12-01'
end_date = '2025-12-17'

def stock_prices():
    for ticker in ticker_symbols:
        data = yf.download(ticker, start = start_date, end = end_date, interval = '1d')

        data["price_change_pct"] = ((data['Close'] - data['Close'].shift(1)) / data['Close'].shift(1)) * 100

        for i, row in data.iterrows():
            c.execute("INSERT INTO stock_prices(ticker, date, open, close, high, low, volume, price_change_pct) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            (ticker, str(i), float(row['Open']), float(row['Close']), float(row['High']), float(row['Low']), int(row['Volume']), float(row["price_change_pct"])))

stock_prices()

conn.commit()
conn.close()