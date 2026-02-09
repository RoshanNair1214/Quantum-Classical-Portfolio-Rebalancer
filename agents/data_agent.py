import yfinance as yf
import pandas as pd

class DataRetrievalAgent:
    def __init__(self, tickers):
        self.tickers = tickers
        self.data = None

    def fetch_data(self, start_date, end_date):
        """Fetches Adjusted Close prices for the cohort."""
        raw_data = yf.download(self.tickers, start=start_date, end=end_date)
        self.data = raw_data['Adj Close'] # AdjClose is the gold standard [cite: 39]
        return self.data

    def get_returns(self):
        """Calculates daily percentage returns."""
        return self.data.pct_change().dropna()
