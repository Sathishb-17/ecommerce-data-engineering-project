import pandas as pd

df = pd.read_csv("dataset/ecommerce_sales.csv")

print(df.head())
print(df.info())
print(df.shape)