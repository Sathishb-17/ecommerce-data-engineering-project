import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

# 1. Category-wise sales
category_sales = pd.read_sql_query("""
SELECT category,
       SUM(total_sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC
""", conn)

category_sales.to_csv("reports/category_sales.csv", index=False)


# 2. Region-wise sales
region_sales = pd.read_sql_query("""
SELECT region,
       SUM(total_sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC
""", conn)

region_sales.to_csv("reports/region_sales.csv", index=False)


# 3. Top 5 products
top_products = pd.read_sql_query("""
SELECT product_id,
       SUM(total_sales) AS total_sales
FROM sales
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5
""", conn)

top_products.to_csv("reports/top_products.csv", index=False)


# 4. Payment method sales
payment_sales = pd.read_sql_query("""
SELECT payment_method,
       SUM(total_sales) AS total_sales
FROM sales
GROUP BY payment_method
ORDER BY total_sales DESC
""", conn)

payment_sales.to_csv("reports/payment_sales.csv", index=False)


conn.close()

print("Reports generated successfully!")