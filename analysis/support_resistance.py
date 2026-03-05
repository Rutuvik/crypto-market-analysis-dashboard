def support_resistance(df):

    support = df["low"].nsmallest(2).values
    resistance = df["high"].nlargest(2).values

    return support, resistance