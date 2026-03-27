def generate_signal(df):
    latest = df.iloc[-1]

    score = 0

    # Trend
    if latest["SMA_50"] > latest["SMA_200"]:
        score += 2
    else:
        score -= 2

    # RSI
    if latest["RSI"] < 30:
        score += 2
    elif latest["RSI"] > 70:
        score -= 2

    # Volatility
    if latest["Volatility"] < 0.02:
        score += 1
    else:
        score -= 1

    return score