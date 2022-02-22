import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
# Simple Stock Price App
## Closing stock price and Volume of Google
""")

tickerSymbol = 'GOOGL'
tickerSymbol1 = 'TSLA'
tickerSymbol2 = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)
tickerData1 = yf.Ticker(tickerSymbol1)
tickerData2 = yf.Ticker(tickerSymbol2)

tickerDf = tickerData.history(period ='1d', start = '2010-1-1', end = '2020-1-31')
tickerDf1 = tickerData1.history(period ='1d', start = '2010-1-1', end = '2020-1-31')
tickerDf2 = tickerData2.history(period ='1d', start = '2010-1-1', end = '2020-1-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Closing stock price and Volume of Tesla
""")

st.write("""
### Closing Price
""")
st.line_chart(tickerDf1.Close)
st.write("""
### Volume
""")
st.line_chart(tickerDf1.Volume)

st.write("""
## Closing stock price and Volume of Apple
""")

st.write("""
## Closing Price
""")
st.line_chart(tickerDf2.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf2.Volume)
