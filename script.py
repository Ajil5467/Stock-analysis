
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

icici = yf.Ticker("ICICIBANK.NS")
hist = icici.history(period="1000d")

data_df = yf.download("AAPL", start="2017-07-01", end="2020-05-01")
data_df.to_csv('stock.csv')

df = pd.read_csv("stock.csv")
df['return'] = ((df['Close'] - df['Open'])/df['Open']).round(2)
df['return'].hist()
