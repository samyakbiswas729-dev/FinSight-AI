def final_decision(score, predictions):
    future_trend = predictions[-1] - predictions[0]

    if future_trend > 0:
        score += 2
    else:
        score -= 2

    if score >= 4:
        return "STRONG BUY"
    elif score >= 2:
        return "BUY"
    elif score <= -3:
        return "SELL"
    else:
        return "HOLD"