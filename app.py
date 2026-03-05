import streamlit as st
from streamlit_autorefresh import st_autorefresh
from analysis.ml_model import train_model
from analysis.pattern_detection import detect_pattern
from data.fetch_crypto_data import get_crypto_data
from analysis.trend import add_indicators, detect_trend
from analysis.support_resistance import support_resistance
from charts.chart_plot import plot_chart


st.set_page_config(page_title="Crypto Market Dashboard", layout="wide")

st.title("📈 Crypto Market Intelligence Dashboard")

st.caption("Real-time crypto analytics with technical indicators")


st_autorefresh(interval=60000, key="refresh")


coins = {
    "Bitcoin":"BTCUSDT",
    "Ethereum":"ETHUSDT",
    "Solana":"SOLUSDT",
    "Chainlink":"LINKUSDT",
    "Polygon":"MATICUSDT"
}


coin_name = st.selectbox("Select Crypto", list(coins.keys()))

coin_symbol = coins[coin_name]


timeframe_options = {
    "1 Week":{"interval":"1h","limit":168},
    "1 Month":{"interval":"4h","limit":180},
    "3 Months":{"interval":"12h","limit":180},
    "6 Months":{"interval":"1d","limit":180}
}


timeframe_label = st.selectbox("Select Timeframe", list(timeframe_options.keys()))


interval = timeframe_options[timeframe_label]["interval"]

limit = timeframe_options[timeframe_label]["limit"]


df = get_crypto_data(symbol=coin_symbol, interval=interval, limit=limit)


if df.empty:

    st.warning("Market data unavailable")

    st.stop()


df = add_indicators(df)


df = df.dropna()


trend = detect_trend(df)


support, resistance = support_resistance(df)
pattern=detect_pattern(df)
ml_direction,ml_prob = train_model(df)

current_price = df["close"].iloc[-1]


col1, col2, col3, col4 = st.columns(4)


col1.metric("Price", f"${current_price:,.2f}")

col2.metric("Trend", trend)

col3.metric("RSI", f"{df['rsi'].iloc[-1]:.2f}")

col4.metric("ML Signal",f"{ml_direction}({ml_prob:.2f})")


fig = plot_chart(df, support, resistance)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Market Commentary")

st.write(f"""
{coin_name} is currently trading at **${current_price:,.2f}**.

Technical trend based on moving averages indicates a **{trend}** market.

The ML model predicts **{ml_direction} movement with {ml_prob:.2f} probability**.

A **{pattern}** pattern has been detected on the chart.

Support levels appear near **{support:.2f}** while resistance levels are forming near **{resistance:.2f}**.

RSI currently stands at **{df['rsi'].iloc[-1]:.2f}**, indicating market momentum conditions.
""")