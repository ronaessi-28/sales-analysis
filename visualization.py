import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('superstore_sales.csv')

# Sales by category
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(6, 4))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Category')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.show()

# Profit vs Discount scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category')
plt.title('Profit vs Discount')
plt.tight_layout()
plt.show()
