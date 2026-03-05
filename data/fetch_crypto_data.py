import requests
import pandas as pd


def get_crypto_data(symbol="bitcoin", interval="1h", limit=200):

    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": "30"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "prices" not in data:
        return pd.DataFrame()

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "close"])

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    df["open"] = df["close"]
    df["high"] = df["close"]
    df["low"] = df["close"]
    df["volume"] = 0

    df = df.rename(columns={"timestamp": "open_time"})

    return df