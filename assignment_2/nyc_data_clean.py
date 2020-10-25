
import pandas as pd

df = pd.read_csv("nyc-rolling-sales.csv")
df = df.rename(columns={'SALE PRICE': 'sale_price'})

