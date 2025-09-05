# Importing modules
import matplotlib.pyplot as plt
import pandas as pandas
import yfinance as yf
import torch

# Importing other python files
from src.load_data import LoadData
from src.populate_dataframe import ProcessData

# Market properties
ticker_symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2020-12-31"

# Loading and processing the data
raw = LoadData(ticker_symbol,start_date,end_date,save=True)
processed = ProcessData(raw,save=True)

plt.plot(processed["Close"])
plt.plot(processed["SMA_10"])
plt.plot(processed["SMA_50"])
plt.plot(processed["Volatility_20"] * 1000)
plt.show()