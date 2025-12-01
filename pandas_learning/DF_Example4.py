import pandas as pd
import numpy as np

# Create comprehensive sales dataset
np.random.seed(42)
data = {
        'Date': pd.date_range ('2025-01-01',periods = 100, freq = 'D'),
        'Product': np.random.choice(['Laptop','Phone','Tablet','Headphones','Charger'],100),
        'Category': np.random.choice(['Electronics','Accessories'], 100),
        'Sales_Amount': np.random.randint(500,50000,100),
        'Quantity': np.random.randint(1,10,100),
        'Customer_Type': np.random.choice(['Regular','Premium','New'], 100),
        'Region': np.random.choice(['North','South','East','West'], 100),
        'Discount_Percent': np.random.randint(0,30,100),
        'Payment_Method': np.random.choice(['Cash','Card','UPI','Wallet'], 100)
        }
df = pd.DataFrame(data)

# Add Calculated Columns
df['Revenue'] = df['Sales_Amount'] * df['Quantity']
df['Discount_Amount'] = df['Revenue'] * df['Discount_Percent'] / 100
df['Final_Revenue'] = df['Revenue'] - df['Discount_Amount']

print(df.head(10))
print("\n")
print(df.info())

print("="*60)
print("LESSON: Boolean Indexing - Filter Sales Above 30,000")
print("="*60)

# Step1: Create the condition (True/False for each row)
condition = df['Sales_Amount']>30000
print("\nStep1: The condition (First 10 rows):")
print(condition.head(10))

# Step2: Count how many True values
print(f"\nHow many sales above 30,000? {condition.sum()}")

# Step3: Use the condition to filter
high_sales = df[condition]

print(f"\nStep3: Filtered Data(showing selected columns):")

print(high_sales[['Date','Product','Sales_Amount','Region']].head(10))

print(f"\nTotal high-value sales: {len(high_sales)} out of {len(df)}")
print(f"Percentage: {len(high_sales)/len(df)*100:.1f}%")



