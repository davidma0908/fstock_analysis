import streamlit as st
import yfinance as yf
import pandas as pd

# Function to get stock news (using yfinance library)
def get_stock_news(ticker):
    stock = yf.Ticker(ticker)
    return stock.news

# Function to get stock financials data
def get_stock_financials(ticker):
    stock = yf.Ticker(ticker)
    return stock.financials, stock.balance_sheet, stock.cashflow

# Function to get stock historical data
def get_stock_historical_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

# Function to get stock name and current price
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    name = stock.info['shortName']
    price = stock.history(period='1d')['Close'].iloc[-1]  # Current closing price
    return name, price


# Apply center alignment to the title using Markdown with HTML
st.markdown('<h1 style="text-align: center; margin-bottom: 20px; '
            'color: #1f77b4; text-shadow: 2px 2px #aaaaaa;">'
            'Stock Information App</h1>', unsafe_allow_html=True)

# User input for stock ticker
ticker = st.text_input('Enter Stock Ticker (e.g., AAPL, MSFT):', 'AAPL')

if ticker:
    # Display stock name and current price in large font
    name, price = get_stock_info(ticker)
    st.markdown(f'<h1 style="text-align: center; margin-bottom: 10px;">{name}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="text-align: center; margin-bottom: 20px;">Current Price: ₹{price:.2f}</h2>', unsafe_allow_html=True)

    # Display stock news
    st.header('Stock News')
    
    # Fetch and display news
    news = get_stock_news(ticker)
    if news:
        for article in news:
            st.markdown(
                f'<div style="border: 1px solid #e6e6e6; border-radius: 5px; padding: 10px; margin-bottom: 10px;">'
                f'<h4>{article["title"]}</h4>'
                f'<p style="color: #666666;">{article["publisher"]}</p>'
                f'<a href="{article["link"]}" target="_blank">Read more</a>'
                f'</div>',
                unsafe_allow_html=True
            )
    else:
        st.write('No news found.')

    # Display stock financials
    st.header('Stock Financials Data')
    financials, balance_sheet, cashflow = get_stock_financials(ticker)

    st.subheader('Income Statement')
    st.write(financials)

    st.subheader('Balance Sheet')
    st.write(balance_sheet)

    st.subheader('Cash Flow')
    st.write(cashflow)

    # Display stock historical data
    st.header('Stock Historical Data')
    period = st.selectbox('Select Period:', ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    historical_data = get_stock_historical_data(ticker, period)
    st.write(historical_data)
    
    # Plot historical data
    st.line_chart(historical_data['Close'])

# Thank you message
st.markdown('<h3 style="text-align: center; margin-top: 20px;">Thank You For Visiting</h3>', unsafe_allow_html=True)
