import pandas as pd
import numpy as np

# Create comprehensive sales dataset
np.random.seed(42)

data = {
    'Date' : pd.date_range('2025-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['Laptop','Phone','Tablet','Headphones','Charger'],100),
    'Category': np.random.choice(['Electronics','Accessories'],100),
    'Sales_Amount': np.random.randint(500,50000,100),
    'Quantity': np.random.randint(1,10,100),
    'Customer_Type': np.random.choice(['Regular','Premium','New'],100),
    'Region': np.random.choice(['North','South','East','West'],100),
    'Discount_percent': np.random.randint(0,30,100),
    'Payment_Method': np.random.choice(['Cash','Card','UPI','Wallet'],100)
    }
df = pd.DataFrame(data)
print(df)

# Add Calculated Column

