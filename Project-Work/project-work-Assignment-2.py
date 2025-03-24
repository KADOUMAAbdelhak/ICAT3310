# PROJECT-WORK-2: Analytics on Cleaned Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine, text
from joblib import dump

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
# 2. Descriptive Analytics
# ---------------------------

print("\n--- Descriptive Statistics: Sales Data ---")
print(sales_df.describe())

# Histogram of Height
plt.hist(sales_df["Height"], bins=15, color='skyblue')
plt.title("Height Distribution")
plt.xlabel("Height (Inches)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

if 'Category' in product_df.columns:
    product_df['Category'].value_counts().plot(kind='bar', color='salmon')
    plt.title("Product Count by Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 3. Predictive Analytics (Simple Regression)
# ---------------------------

X = sales_df[["Height"]]
y = sales_df["Weight"]

model = LinearRegression()
model.fit(X, y)
sales_df['Predicted_Weight'] = model.predict(X)

# Plot regression line
plt.scatter(sales_df['Height'], sales_df['Weight'], label='Actual')
plt.plot(sales_df['Height'], sales_df['Predicted_Weight'], color='red', label='Predicted')
plt.xlabel("Height (Inches)")
plt.ylabel("Weight (Pounds)")
plt.title("Predicting Weight from Height")
plt.legend()
plt.tight_layout()
plt.show()

# Save the model
dump(model, "height_weight_model.joblib")

# ---------------------------
# 4. Prescriptive Analytics (Profit Optimization)
# ---------------------------

if {'Sales', 'Profit'}.issubset(product_df.columns):
    product_df['Profit_Margin'] = product_df['Profit'] / product_df['Sales']
    top_products = product_df.sort_values(by='Profit_Margin', ascending=False).head(10)
    print("\nTop 10 Products by Profit Margin:")
    print(top_products[['Product_Name', 'Sales', 'Profit', 'Profit_Margin']])

    # Plot
    plt.figure(figsize=(10,5))
    sns.barplot(data=top_products, x='Product_Name', y='Profit_Margin')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 10 Products by Profit Margin")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 5. Save Processed Data
# ---------------------------

sales_df.to_csv("analytics_output_sales.csv", index=False)
product_df.to_csv("analytics_output_products.csv", index=False)
print("\n✅ Analytics complete. Outputs saved.")
