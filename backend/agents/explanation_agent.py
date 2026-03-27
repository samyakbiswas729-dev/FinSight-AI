import os

class ExplanationAgent:
    def __init__(self):
        # Secure way (no hardcoded key)
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate_explanation(self, decision, indicators, sentiment):
        """
        Generates explanation for trading decision
        """

        explanation = f"""
        📊 Trading Decision Explanation:

        Decision: {decision}

        🔹 Technical Indicators:
        {indicators}

        🔹 Market Sentiment:
        {sentiment}

        💡 Reason:
        The decision is based on combined analysis of technical indicators 
        and sentiment trends. Positive signals suggest buying, negative suggest selling.

        ⚠️ Note:
        This is AI-generated insight and not financial advice.
        """

        return explanation
        