import pandas as pd
from sqlalchemy import create_engine
import sqlite3

df = pd.read_csv(
    "dataset/ecommerce_sales.csv"
)
df["order_date"] = pd.to_datetime(df["order_date"])

df = df.drop_duplicates()

df["total_sales"] = df["price"] * df["quantity"]

engine = create_engine(
    "sqlite:///database/ecommerce.db"
)

df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully")




conn = sqlite3.connect(
    "database/ecommerce.db"
)

query = """
SELECT *
FROM sales
LIMIT 5
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()