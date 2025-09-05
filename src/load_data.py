import yfinance as yf
import matplotlib.pyplot as plt

def LoadData(ticker_symbol = "AAPL", start_date="2020-01-01", end_date="2020-12-31"):
    ticker = yf.Ticker(ticker=ticker_symbol)
    history = ticker.history(start=start_date,end=end_date)
    history.to_csv(f"../data/raw/{ticker_symbol}_{start_date}_{end_date}.csv")
    return history