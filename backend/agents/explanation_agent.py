def explain(decision, indicators, sentiment):
    return f"""
📊 Trading Decision: {decision}

🔹 Indicators:
{indicators}

🔹 Sentiment:
{sentiment}

💡 Explanation:
Based on combined technical indicators and market sentiment, 
the model suggests a {decision} action.

⚠️ Not financial advice.
"""