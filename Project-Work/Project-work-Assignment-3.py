# PROJECT-WORK-3: KPI Creation and Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import json

# ---------------------------
# 1. Load Cleaned Data from SQLite
# ---------------------------

db_path = 'sqlite:///system_data.db'
engine = create_engine(db_path)

# Load tables
sales_df = pd.read_sql("sales_data", engine)
product_df = pd.read_sql("product_data", engine)
exchange_df = pd.read_sql("exchange_rates", engine)
supplier_df = pd.read_sql("supplier_data", engine)

# Clean column names again if needed
sales_df.columns = sales_df.columns.str.strip().str.replace('"', '').str.replace("'", '')
sales_df.rename(columns={
    "Height(Inches)": "Height",
    "Weight(Pounds)": "Weight"
}, inplace=True)

# ---------------------------
# 2. Define and Save KPIs
# ---------------------------

kpis = {}

# KPI 1: Average Weight
kpis['Average_Weight'] = round(sales_df['Weight'].mean(), 2)

# KPI 2: Number of Products
kpis['Number_of_Products'] = len(product_df)

# KPI 3: Average Sales per Product
if 'Sales' in product_df.columns:
    kpis['Average_Sales_per_Product'] = round(product_df['Sales'].mean(), 2)

# KPI 4: Number of Suppliers
kpis['Number_of_Suppliers'] = len(supplier_df)

# KPI 5: EUR to USD Exchange Rate
kpis['EUR_to_USD_Rate'] = exchange_df.loc[0, 'rate'] if not exchange_df.empty else None

# Save KPIs to JSON
with open("project_kpis.json", "w") as f:
    json.dump(kpis, f, indent=4)

print("\n✅ KPIs saved to project_kpis.json")

# ---------------------------
# 3. Create and Save KPI Visualizations
# ---------------------------

# Bar chart for KPI comparison
plt.figure(figsize=(8, 4))
plt.bar(kpis.keys(), kpis.values(), color='teal')
plt.title("Project KPIs Overview")
plt.ylabel("Values")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("kpi_overview.png")
plt.show()

# Histogram for Weight distribution
plt.figure(figsize=(6, 4))
plt.hist(sales_df['Weight'], bins=15, color='orange')
plt.title("Weight Distribution")
plt.xlabel("Weight (Pounds)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("weight_distribution.png")
plt.show()

# Product count by Category
if 'Category' in product_df.columns:
    plt.figure(figsize=(6, 4))
    product_df['Category'].value_counts().plot(kind='bar', color='purple')
    plt.title("Product Count by Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("product_category_distribution.png")
    plt.show()

print("\n✅ KPI visualizations saved.")
