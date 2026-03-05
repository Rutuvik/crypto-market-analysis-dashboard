import pandas_ta as ta


def add_indicators(df):

    df["ma20"] = ta.sma(df["close"], length=20)
    df["ma50"] = ta.sma(df["close"], length=50)

    df["rsi"] = ta.rsi(df["close"], length=14)

    return df


def detect_trend(df):

    # remove NaN values
    df = df.dropna()

    # if dataframe becomes empty return safe value
    if len(df) == 0:
        return "Sideways"

    ma20 = df["ma20"].iloc[-1]
    ma50 = df["ma50"].iloc[-1]

    if ma20 > ma50:
        return "Bullish"
    elif ma20 < ma50:
        return "Bearish"
    else:
        return "Sideways"