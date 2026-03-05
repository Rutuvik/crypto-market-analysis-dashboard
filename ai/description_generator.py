def generate_description(price, trend, pattern, support, resistance):

    text = f"""
    Current price is {price:.2f} USD.

    The market trend is {trend}.

    The chart shows a {pattern} pattern.

    Key support levels are around {support[0]:.2f} and {support[1]:.2f}.

    Resistance levels appear near {resistance[0]:.2f} and {resistance[1]:.2f}.
    """

    return text