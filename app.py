import streamlit as st

from data.fetch_crypto_data import get_crypto_data
from analysis.trend import add_indicators, detect_trend
from analysis.support_resistance import support_resistance
from charts.chart_plot import plot_chart


st.title("Crypto Market Analysis Dashboard")


coins = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
    "Solana": "SOLUSDT",
    "Chainlink": "LINKUSDT",
    "Polygon": "MATICUSDT"
}


coin_name = st.selectbox("Select Crypto", list(coins.keys()))

coin_symbol = coins[coin_name]


timeframe_options = {
    "1 Week": {"interval": "1h", "limit": 168},
    "1 Month": {"interval": "4h", "limit": 180},
    "3 Months": {"interval": "12h", "limit": 180},
    "6 Months": {"interval": "1d", "limit": 180}
}


timeframe_label = st.selectbox(
    "Select Timeframe",
    list(timeframe_options.keys())
)


interval = timeframe_options[timeframe_label]["interval"]
limit = timeframe_options[timeframe_label]["limit"]


df = get_crypto_data(symbol=coin_symbol, interval=interval, limit=limit)


df = add_indicators(df)


trend = detect_trend(df)


support, resistance = support_resistance(df)


current_price = df["close"].iloc[-1]


col1, col2, col3 = st.columns(3)

col1.metric("Price", f"${current_price:,.2f}")

col2.metric("Trend", trend)

rsi_series = df["rsi"].dropna()

if len(rsi_series) > 0:
    rsi_value = rsi_series.iloc[-1]
else:
    rsi_value = 0

col3.metric("RSI", f"{rsi_value:.2f}")

fig = plot_chart(df, support, resistance)

st.plotly_chart(fig, use_container_width=True)



st.subheader("Market Commentary")

st.write(
f"""
{coin_name} is currently trading at ${current_price:,.2f}.
The market trend is **{trend}** based on moving average crossover.

The RSI indicator suggests momentum conditions.
Support levels appear near {support[0]:.2f} and {support[1]:.2f},
while resistance is forming near {resistance[0]:.2f} and {resistance[1]:.2f}.
"""
)