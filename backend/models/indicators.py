import pandas as pd
import numpy as np

def calculate_indicators(df):
    df["SMA_50"] = df["Close"].rolling(50).mean()
    df["SMA_200"] = df["Close"].rolling(200).mean()

    df["Returns"] = df["Close"].pct_change()

    df["Volatility"] = df["Returns"].rolling(20).std()

    df["RSI"] = compute_rsi(df["Close"])

    return df


def compute_rsi(series, period=14):
    delta = series.diff()

    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()

    rs = gain / loss
    return 100 - (100 / (1 + rs))