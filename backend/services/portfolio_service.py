from backend.agents.explanation_agent import explain
import numpy as np


def get_portfolio_analysis(symbol: str):

    decision = np.random.choice(["BUY", "SELL", "HOLD"])
    score = round(np.random.uniform(0.6, 0.95), 2)
    risk = np.random.choice(["Low", "Medium", "High"])

    prediction = list(np.random.uniform(140, 180, 7))

    expected_profit = round(np.random.uniform(500, 5000), 2)
    future_price = round(prediction[-1], 2)

    explanation = explain(decision, "RSI + MACD", "Positive sentiment")

    return {
        "decision": decision,
        "score": score,
        "risk": risk,
        "prediction": prediction,
        "expected_profit": expected_profit,
        "future_price": future_price,
        "explanation": explanation
    }