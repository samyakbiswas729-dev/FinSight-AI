from fastapi import FastAPI
from backend.services.portfolio_service import get_portfolio_analysis
import pandas as pd
import numpy as np

app = FastAPI()


@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    # Dummy stock data (10 years simulated)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=3000)

    prices = np.cumsum(np.random.randn(3000)) + 150
    volume = np.random.randint(1000000, 5000000, size=3000)

    data = pd.DataFrame({
        "Date": dates,
        "Close": prices,
        "Volume": volume
    })

    return {"data": data.to_dict(orient="records")}


@app.get("/portfolio/{symbol}")
def portfolio(symbol: str):
    return get_portfolio_analysis(symbol)