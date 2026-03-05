import plotly.graph_objects as go


def plot_chart(df, support, resistance):

    fig = go.Figure()

    # Candlestick
    fig.add_trace(
        go.Candlestick(
            x=df["open_time"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            name="Price"
        )
    )

    # Moving averages
    fig.add_trace(
        go.Scatter(
            x=df["open_time"],
            y=df["ma20"],
            line=dict(color="yellow"),
            name="MA20"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["open_time"],
            y=df["ma50"],
            line=dict(color="blue"),
            name="MA50"
        )
    )

    # Support lines
    for s in support:
        fig.add_hline(y=s, line_dash="dash", line_color="green")

    # Resistance lines
    for r in resistance:
        fig.add_hline(y=r, line_dash="dash", line_color="red")

    fig.update_layout(
        template="plotly_dark",
        height=600,
        xaxis_title="Time",
        yaxis_title="Price (USD)"
    )

    return fig


def plot_rsi(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["open_time"],
            y=df["rsi"],
            line=dict(color="orange"),
            name="RSI"
        )
    )

    fig.add_hline(y=70, line_dash="dash", line_color="red")
    fig.add_hline(y=30, line_dash="dash", line_color="green")

    fig.update_layout(
        template="plotly_dark",
        height=250,
        yaxis_title="RSI"
    )

    return fig