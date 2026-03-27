import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import time

# ⚡ CONFIG
st.set_page_config(page_title="FinSight AI", layout="wide")

# 🎨 FUTURISTIC UI
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(10px);
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 20px rgba(0,255,255,0.2);
    margin-bottom: 20px;
}

/* Neon Title */
.neon {
    color: #00f7ff;
    text-shadow: 0 0 10px #00f7ff, 0 0 20px #00f7ff;
}

/* Metric Glow */
.metric {
    font-size: 22px;
    font-weight: bold;
    color: #00ffcc;
    text-shadow: 0 0 10px #00ffcc;
}

</style>
""", unsafe_allow_html=True)

# 🚀 TITLE
st.markdown('<h1 class="neon">🚀 FinSight AI Dashboard</h1>', unsafe_allow_html=True)

# 📊 STOCK LIST (expandable to 100+)
stock_list = [
"AAPL","MSFT","GOOGL","AMZN","TSLA","NVDA","META","NFLX",
"INFY","TCS.NS","RELIANCE.NS","HDFCBANK.NS","ICICIBANK.NS",
"SBIN.NS","ITC.NS","LT.NS","AXISBANK.NS"
]

symbol = st.selectbox("📌 Select Stock", stock_list)

# 🔄 FETCH DATA
data = requests.get(f"http://127.0.0.1:8000/stock/{symbol}").json()
df = pd.DataFrame(data["data"])

df["Date"] = pd.to_datetime(df["Date"])

# 🎯 ANIMATED METRICS
latest_price = df["Close"].iloc[-1]
prev_price = df["Close"].iloc[-2]

change = latest_price - prev_price
percent = (change / prev_price) * 100

col1, col2, col3 = st.columns(3)

def animated_metric(label, value, suffix=""):
    placeholder = st.empty()
    for i in np.linspace(0, value, 20):
        placeholder.markdown(
            f"<div class='metric'>{label}: {i:.2f}{suffix}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.01)

with col1:
    animated_metric("💰 Price", latest_price)

with col2:
    animated_metric("📊 Change", change)

with col3:
    animated_metric("📈 % Change", percent, "%")

# 📈 PRICE CHART
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("📈 Price Trend (10 Years)")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Date"],
    y=df["Close"],
    mode='lines',
    line=dict(color='#00f7ff', width=2),
    name='Price'
))

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 📊 VOLUME CHART
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("📊 Volume Analysis")

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=df["Date"],
    y=df["Volume"],
    marker_color='#00ffcc'
))

fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.plotly_chart(fig2, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 🥧 PORTFOLIO PIE
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("🥧 Portfolio Allocation")

pie_data = pd.DataFrame({
    "Stock": ["Equity", "Cash", "Bonds"],
    "Value": [70, 20, 10]
})

fig3 = go.Figure(data=[go.Pie(
    labels=pie_data["Stock"],
    values=pie_data["Value"],
    hole=.4
)])

fig3.update_traces(
    marker=dict(colors=['#00f7ff', '#00ffcc', '#0088ff'])
)

fig3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.plotly_chart(fig3, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 🤖 AI ANALYSIS
analysis = requests.get(f"http://127.0.0.1:8000/portfolio/{symbol}").json()

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("🤖 AI Recommendation")

st.markdown(
    f"<div class='metric'>Decision: {analysis['decision']}</div>",
    unsafe_allow_html=True
)

st.write("📊 Score:", analysis["score"])
st.write("⚠️ Risk:", analysis["risk"])
st.info(analysis["explanation"])

st.markdown('</div>', unsafe_allow_html=True)

# 🔮 PREDICTION CHART
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("🔮 AI Price Prediction (Next 7 Days)")

pred = analysis["prediction"]

future_dates = pd.date_range(
    start=df["Date"].iloc[-1],
    periods=7
)

pred_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted Price": pred
})

fig4 = go.Figure()

fig4.add_trace(go.Scatter(
    x=pred_df["Date"],
    y=pred_df["Predicted Price"],
    mode='lines+markers',
    line=dict(color='#ff00ff', width=3),
    name="Prediction"
))

fig4.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.plotly_chart(fig4, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 💼 INVESTMENT SIMULATION
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("💼 Investment Simulation")

st.write(f"💰 Expected Profit: ₹{analysis['expected_profit']}")
st.write(f"📈 Future Price: ₹{analysis['future_price']}")

st.markdown('</div>', unsafe_allow_html=True)