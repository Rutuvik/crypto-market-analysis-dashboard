import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def prepare_features(df):

    df["return"] = df["close"].pct_change()

    df["volatility"] = df["return"].rolling(10).std()

    df["momentum"] = df["close"] - df["close"].shift(10)

    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)

    df = df.dropna()

    X = df[["ma20", "ma50", "rsi", "volatility", "momentum"]]

    y = df["target"]

    return X, y


def train_model(df):

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestClassifier(n_estimators=100)

    model.fit(X_train, y_train)

    prediction = model.predict(X.tail(1))[0]

    probability = model.predict_proba(X.tail(1))[0][prediction]

    if prediction == 1:
        direction = "Bullish"
    else:
        direction = "Bearish"

    return direction, probability