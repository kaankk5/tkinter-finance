import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('historical_data/AVAXUSDT_5m_2d_STOCHRSI_MACD.csv')

# Convert the 'timestamp' column to a datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create the candlestick chart trace
candlestick = go.Candlestick(
    x=df['timestamp'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name='Candlestick'
)


# Display the chart
fig.show()
