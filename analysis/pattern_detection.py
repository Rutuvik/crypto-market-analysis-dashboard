def detect_pattern(df):

    prices = df["close"]

    min_points = prices.nsmallest(2)

    if abs(min_points.iloc[0] - min_points.iloc[1]) < prices.mean() * 0.02:
        return "Double Bottom"

    return "No Clear Pattern"