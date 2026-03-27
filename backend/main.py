from fastapi import FastAPI
from backend.services.portfolio_service import get_portfolio_analysis
from backend.services.learning import get_stock_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FinSight AI Running 🚀"}

@app.get("/stock/{symbol}")
def stock(symbol: str):
    return get_stock_data(symbol)

@app.get("/portfolio/{symbol}")
def portfolio(symbol: str):
    return get_portfolio_analysis(symbol)