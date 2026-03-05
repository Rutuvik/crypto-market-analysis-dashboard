import plotly.graph_objects as go


def plot_chart(df, support, resistance):

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df["open_time"],
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="Price"
    ))

    fig.add_trace(go.Scatter(
        x=df["open_time"],
        y=df["ma20"],
        name="MA20",
        line=dict(color="yellow")
    ))

    fig.add_trace(go.Scatter(
        x=df["open_time"],
        y=df["ma50"],
        name="MA50",
        line=dict(color="blue")
    ))

    fig.add_hline(y=support, line_dash="dash", line_color="green")

    fig.add_hline(y=resistance, line_dash="dash", line_color="red")

    fig.update_layout(
        template="plotly_dark",
        height=600,
        xaxis_rangeslider_visible=False
    )

    return fig