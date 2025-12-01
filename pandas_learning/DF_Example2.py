import pandas as pd
import numpy as np

np.random.seed(99)  # Use different seed

data = {
    'Date': pd.date_range('2025-11-16', periods= 7, freq='D'),
    'Customer': np.random.choice(['Regular','Premium'], 7),
    'Amount': np.random.randint(1000, 10000, 7),
    'Payment': np.random.choice(['Cash','Card','UPI'], 7)
}

df = pd.DataFrame(data)
print(df)

