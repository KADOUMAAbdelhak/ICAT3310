import pandas as pd
import requests
import tabula
from sqlalchemy import create_engine

# ---------------------------
# 1. Load Data from All Sources
# ---------------------------

# 1.1 CSV: Sales/Weight Data
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
sales_df = pd.read_csv(csv_url)
print("\nCSV Data (sales_df):")
print(sales_df.head())

# Clean CSV (remove NaNs, ensure proper types)
sales_df.dropna(inplace=True)
sales_df.columns = [col.strip() for col in sales_df.columns] 

# 1.2 Excel: Product Info
excel_path = "Sample - Superstore.xls" 
product_df = pd.read_excel(excel_path)
print("\nExcel Data (product_df):")
print(product_df.head())

# Clean Excel
product_df.dropna(subset=["Product Name"], inplace=True)
product_df.columns = [col.strip().replace(" ", "_") for col in product_df.columns]

# 1.3 API: Currency Exchange Rate
api_url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(api_url)
exchange_data = response.json()
eur_to_usd = exchange_data['rates'].get('EUR', None)
print(f"\nEUR to USD rate: {eur_to_usd}")

# Prepare exchange DataFrame
exchange_df = pd.DataFrame([{"base": "USD", "target": "EUR", "rate": eur_to_usd}])

# 1.4 PDF: Supplier Table
pdf_path = "datatable.pdf"
pdf_tables = tabula.read_pdf(pdf_path, pages='all')
supplier_df = pdf_tables[0] if pdf_tables else pd.DataFrame()
print("\nPDF Table (supplier_df):")
print(supplier_df.head())

# Clean PDF Table
supplier_df.dropna(how="all", inplace=True)
supplier_df.columns = [col.strip().replace(" ", "_") for col in supplier_df.columns]

# ---------------------------
# 2. Create SQLite DB and Store Data
# ---------------------------

# Create SQLite database
engine = create_engine('sqlite:///system_data.db')

# Save each DataFrame to SQL
sales_df.to_sql("sales_data", engine, index=False, if_exists='replace')
product_df.to_sql("product_data", engine, index=False, if_exists='replace')
exchange_df.to_sql("exchange_rates", engine, index=False, if_exists='replace')
supplier_df.to_sql("supplier_data", engine, index=False, if_exists='replace')

print("\n All data saved to SQLite database: system_data.db")


