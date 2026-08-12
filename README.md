# E-Commerce Data Engineering Project

##  Project Overview

This project demonstrates an end-to-end ETL pipeline for processing
e-commerce sales data using Python, Pandas, and SQLite.

The pipeline extracts raw sales data from a CSV file, cleans and
transforms the data, loads it into a SQLite database, and generates
business analysis reports using SQL.

##  ETL Workflow

CSV Dataset
    ↓
Extract
    ↓
Clean & Transform
    ↓
SQLite Database
    ↓
SQL Analysis
    ↓
Reports

##  Technologies Used

- Python
- Pandas
- SQL
- SQLite
- SQLAlchemy
- Git
- GitHub

##  Project Structure

```text
ecommerce-data-engineering-project/
│
├── dataset/
│   └── ecommerce_sales.csv
│
├── database/
│   └── ecommerce.db
│
├── scripts/
│   ├── etl_pipeline.py
│   └── analysis.py
│
├── reports/
│   ├── category_sales.csv
│   ├── region_sales.csv
│   ├── top_products.csv
│   └── payment_sales.csv
│
├── requirements.txt
└── README.md