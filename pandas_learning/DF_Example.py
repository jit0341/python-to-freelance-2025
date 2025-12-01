import pandas as pd
import numpy as np

# 1.Setup
np.random.seed(42)
# 2. Create Dictionary
data = {
    'Date': pd.date_range('2025-01-01', periods = 5, freq = 'D'),
    'Product': np.random.choice(['Laptop','Phone','Tablet']),
    'Sales': np.random.randint(10000,50000,5),
    'Region': np.random.choice(['North','South'],5)
    }
# 3. Convert to DataFrame
df = pd.DataFrame(data)

# 4 Display

print(df)
print("\n")
print("DataFrame info:")
print(df.info())


