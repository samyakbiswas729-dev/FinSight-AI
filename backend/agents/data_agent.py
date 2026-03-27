from backend.models.indicators import calculate_indicators

def process_data(df):
    return calculate_indicators(df)