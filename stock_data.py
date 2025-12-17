import pandas as pd
import yfinance as yf
from news_headline_scraper import ticker_symbols 

start_date = '2024-01-01'
end_date = '2025-01-01'

def stock_prices():

    for ticker in ticker_symbols:
        ticker = yf.Ticker(ticker)
        data = yf.download(ticker, start = start_date, end = end_date, interval = '1d')

