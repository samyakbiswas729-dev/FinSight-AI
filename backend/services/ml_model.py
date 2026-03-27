from sklearn.linear_model import LinearRegression
import numpy as np

def predict_prices(df):
    df = df.dropna().copy()

    df["Day"] = np.arange(len(df))

    X = df[["Day"]]
    y = df["Close"]

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.arange(len(df), len(df) + 7).reshape(-1, 1)
    predictions = model.predict(future_days)

    return predictions.tolist()