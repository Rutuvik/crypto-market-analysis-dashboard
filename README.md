# Crypto Market Analysis Dashboard

A real-time **cryptocurrency market intelligence dashboard** built using Python and Streamlit.
This application provides interactive financial analytics for selected crypto assets using **live market data**, technical indicators, and automated chart analysis.

The system allows users to explore market trends, visualize price action, and understand the current market structure through **chart-based analytics and dynamic commentary**.

---

# Live Deployment

Live Application
https://crypto-market-analysis-dashboard.streamlit.app/


GitHub Repository
[https://github.com/Rutuvik/crypto-market-analysis-dashboard](https://github.com/Rutuvik/crypto-market-analysis-dashboard)

---

# Project Objective

The goal of this project is to build an **interactive cryptocurrency market analysis module** that allows users to analyze selected crypto assets using **real-time market data and technical indicators**.

The application provides a financial dashboard that displays price charts, identifies market trends, calculates support and resistance levels, and generates human-readable market insights.

All displayed data is fetched **live from external APIs at runtime**, ensuring the dashboard reflects the current market conditions.

---

# Supported Crypto Assets

The dashboard analyzes five cryptocurrencies representing different sectors of the crypto ecosystem.

| Asset     | Category                 |
| --------- | ------------------------ |
| Bitcoin   | Store of Value           |
| Ethereum  | Smart Contract Platform  |
| Solana    | High Performance Layer 1 |
| Chainlink | Oracle Infrastructure    |
| Polygon   | Layer 2 Scaling          |

These assets were selected to ensure diversity across major crypto market categories.

---

# Core Features

## Live Market Data

All market data is fetched dynamically using the Binance public API.
This ensures that the dashboard always reflects the latest available market prices and trading activity.

Data retrieved includes:

* Open price
* High price
* Low price
* Close price
* Volume

The application does not use any static datasets or locally stored files.

---

## Interactive Candlestick Charts

Price action is visualized using interactive candlestick charts built with Plotly.

The charts display OHLC data and allow users to analyze price behavior across multiple timeframes.

Supported timeframes include:

* 1 Week
* 1 Month
* 3 Months
* 6 Months

---

## Technical Indicators

The dashboard incorporates commonly used technical indicators to provide analytical insights.

### Moving Averages

Two moving averages are calculated to identify market trends:

* 20-period Moving Average
* 50-period Moving Average

Trend direction is derived from the relationship between these indicators.

### Relative Strength Index (RSI)

RSI is used to analyze market momentum and determine whether an asset is approaching overbought or oversold conditions.

---

## Trend Detection

The system automatically determines the current market trend using moving average crossover logic.

Trend classifications include:

* Bullish
* Bearish
* Sideways

This provides users with a quick interpretation of market direction.

---

## Support and Resistance Levels

Key price levels are calculated programmatically using recent price extremes.

These levels are displayed on the chart and represent areas where:

* Buying pressure may increase (Support)
* Selling pressure may increase (Resistance)

These levels help users identify potential breakout or reversal zones.

---

## Dynamic Market Commentary

Below each chart, the application generates a text-based market summary describing the current market situation.

The commentary includes:

* Current asset price
* Trend direction
* Momentum conditions
* Key support levels
* Key resistance levels

This provides a quick human-readable explanation of the chart.

---

# System Architecture

The application follows a modular architecture separating data processing, analysis, and visualization.

```
crypto-dashboard
│
├── app.py
│
├── data
│   └── fetch_crypto_data.py
│
├── analysis
│   ├── trend.py
│   └── support_resistance.py
│
├── charts
│   └── chart_plot.py
│
└── requirements.txt
```

### Data Layer

Handles real-time data retrieval from the Binance API.

### Analysis Layer

Processes market data and calculates indicators such as moving averages, RSI, and support/resistance levels.

### Visualization Layer

Responsible for rendering interactive charts and the dashboard interface.

---

# Technology Stack

| Component            | Technology  |
| -------------------- | ----------- |
| Programming Language | Python      |
| Dashboard Framework  | Streamlit   |
| Data Processing      | Pandas      |
| Technical Indicators | Pandas TA   |
| Visualization        | Plotly      |
| Market Data Source   | Binance API |

---

# Installation

Clone the repository:

```
git clone https://github.com/Rutuvik/crypto-market-analysis-dashboard.git
cd crypto-market-analysis-dashboard
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

The dashboard will start locally at:

```
http://localhost:8501
```

---

# Future Improvements

Potential enhancements for the system include:

* Advanced chart pattern detection
* Volatility analysis
* Market sentiment indicators
* Real-time price updates using WebSockets
* Portfolio tracking features
* AI-generated market insights

---

# Author

Rutvik Chavhan

---

# Notes

This project was developed as part of a technical assignment to demonstrate the ability to build a full-stack financial analytics module using live market data and technical analysis techniques.
