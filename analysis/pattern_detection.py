import numpy as np


def detect_pattern(df):

    prices = df["close"].values

    peaks = []

    for i in range(2, len(prices) - 2):

        if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
            peaks.append(i)

    if len(peaks) >= 2:

        p1 = peaks[-2]
        p2 = peaks[-1]

        if abs(prices[p1] - prices[p2]) / prices[p1] < 0.02:
            return "Double Top"

    troughs = []

    for i in range(2, len(prices) - 2):

        if prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
            troughs.append(i)

    if len(troughs) >= 2:

        t1 = troughs[-2]
        t2 = troughs[-1]

        if abs(prices[t1] - prices[t2]) / prices[t1] < 0.02:
            return "Double Bottom"

    return "No Pattern"