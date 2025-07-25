import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
 
# Load the data 
df = pd.read_csv('superstore_sales.csv')

# Convert columns to numeric
df['Sales'] = df['Sales'].astype(float)
df['Profit'] = df['Profit'].astype(float)
df['Discount'] = df['Discount'].astype(float)

# ---------- Sales by Category ----------
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(6, 4))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Category')
plt.ylabel('Sales (₹)')
plt.tight_layout()
plt.show()

# ---------- Sales by City ----------
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 4))
city_sales.plot(kind='bar', color='orange')
plt.title('Top 5 Cities by Sales')
plt.ylabel('Sales (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Profit by City ----------
city_profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 4))
city_profit.plot(kind='bar', color='green')
plt.title('Top 5 Cities by Profit')
plt.ylabel('Profit (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Average Discount by City ----------
city_discount = df.groupby('City')['Discount'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 4))
city_discount.plot(kind='bar', color='purple')
plt.title('Top 5 Cities by Average Discount')
plt.ylabel('Average Discount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Profit vs Discount Scatter ----------
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='City')
plt.title('Profit vs Discount by City')
plt.tight_layout()
plt.show()
