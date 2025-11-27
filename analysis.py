import pandas as pd
   
# Load the data     
df = pd.read_csv('superstore_sales.csv') 
     
# Ensure correct data types     
df['Sales'] = df['Sales'].astype(float)  
df['Profit'] = df['Profit'].astype(float) 
df['Discount'] = df['Discount'].astype(float)  

# Convert date columns with Indian format (DD/MM/YYYY)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# Basic info
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print(f"\nTotal Sales: ₹{total_sales:,.2f}")

# Top 5 cities by sales
top_cities_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Cities by Sales:\n", top_cities_sales.to_string())

# Top 5 cities by profit
top_cities_profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Cities by Profit:\n", top_cities_profit.to_string())
# Top 5 cities by average discount
top_cities_discount = df.groupby('City')['Discount'].mean().sort_values(ascending=False).head(5)
print("\nTop 5 Cities by Average Discount:\n", top_cities_discount.round(2).to_string())
