from src.load_data import LoadData
import pandas

def ProcessData(df,save=False):
    df["Return"] = df["Close"].pct_change()
    df["SMA_10"] = df["Close"].rolling(window=10).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["Volatility_20"] = df["Return"].rolling(window=20).std()
    if save:
        df.to_csv(f"data/processed/{df["Ticker"].iloc[0]}_{df["Start"].iloc[0]}_{df["End"].iloc[0]}.csv")
    return df