import yfinance as yf

from backend.agents.data_agent import process_data
from backend.agents.signal_agent import generate_signal
from backend.agents.decision_agent import final_decision
from backend.agents.explanation_agent import explain
from backend.services.ml_model import predict_prices


def get_portfolio_analysis(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history(period="10y")

    df = process_data(df)

    score = generate_signal(df)

    predictions = predict_prices(df)

    decision = final_decision(score, predictions)

    explanation = explain(score, decision)

    latest_price = df["Close"].iloc[-1]

    investment = 10000
    shares = investment / latest_price

    future_price = predictions[-1]

    future_value = shares * future_price
    profit = future_value - investment

    return {
        "symbol": symbol,
        "decision": decision,
        "score": score,
        "prediction": predictions,
        "expected_profit": round(profit, 2),
        "future_price": round(future_price, 2),
        "risk": "High" if df["Volatility"].iloc[-1] > 0.03 else "Moderate",
        "explanation": explanation
    }