import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    'Date': pd.date_range('2025-01-01', periods = 10, freq= 'D'),
    'Product': np.random.choice(['Laptop','Phone','Tablet'],10),
    'Price': np.random.randint(10000,50000,10)
    }
print("This is a Dictionary.")
print(data)
print("\nType:", type(data))
df = pd.DataFrame(data)
print("\nThis is DataFrame:")
print(df)
print("\nType:", type(df))




