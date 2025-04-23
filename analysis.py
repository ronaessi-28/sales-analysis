import pandas as pd

# Load the data
df = pd.read_csv('superstore_sales.csv')

# Basic info
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Total sales
total_sales = df['Sales'].sum()
print(f"\nTotal Sales: ${total_sales:.2f}")

# Top 5 states by sales
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States by Sales:\n", top_states)

# Average discount
avg_discount = df['Discount'].mean()
print(f"\nAverage Discount: {avg_discount:.2f}")
