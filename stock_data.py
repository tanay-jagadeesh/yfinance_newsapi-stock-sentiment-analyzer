import pandas as pd
import yfinance as yf
from news_headline_scraper import ticker_symbols 


def stock_prices():

    for ticker in ticker_symbols:
        ticker = yf.Ticker(ticker)