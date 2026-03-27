import yfinance as yf

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="10y")

    df.reset_index(inplace=True)

    return {
        "symbol": symbol,
        "data": df.to_dict(orient="records")
    }