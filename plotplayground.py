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

indicator_traces = []

# Loop through the indicators and create traces dynamically
indicators = ['indicator1', 'indicator2', 'indicator3']  # Replace with your actual indicator column names
for indicator in indicators:
    trace = go.Scatter(
        x=df['timestamp'],
        y=df[indicator],
        mode='lines',
        name=indicator
    )
    indicator_traces.append(trace)

# Create a figure with the candlestick trace and indicator traces
data = [candlestick] + indicator_traces
layout = go.Layout(
    title='Price Chart with Indicators',
    xaxis=dict(title='Time'),
    yaxis=dict(title='Price'),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
)
fig = go.Figure(data=data, layout=layout)

# Display the chart
fig.show()



# Create a figure with the candlestick trace
fig = go.Figure(data=candlestick)

# Customize the layout
fig.update_layout(
    title='Stock Data',
    xaxis_title='Time',
    yaxis_title='Price',
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
)

# Display the chart
fig.show()