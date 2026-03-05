import requests
import pandas as pd

PRODUCTS = {
    "BTCUSDT": "BTC-USD",
    "ETHUSDT": "ETH-USD",
    "SOLUSDT": "SOL-USD",
    "LINKUSDT": "LINK-USD",
    "MATICUSDT": "MATIC-USD"
}

INTERVAL_MAP = {
    "1h": 3600,
    "4h": 14400,
    "12h": 43200,
    "1d": 86400
}


def get_crypto_data(symbol="BTCUSDT", interval="1h", limit=200):

    product = PRODUCTS[symbol]

    granularity = INTERVAL_MAP[interval]

    url = f"https://api.exchange.coinbase.com/products/{product}/candles"

    params = {"granularity": granularity}

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, params=params, headers=headers)

    data = r.json()

    if not isinstance(data, list) or len(data) == 0:
        return pd.DataFrame()

    df = pd.DataFrame(data, columns=[
        "time","low","high","open","close","volume"
    ])

    df["open_time"] = pd.to_datetime(df["time"], unit="s")

    df = df[["open_time","open","high","low","close","volume"]]

    df = df.sort_values("open_time")

    return df