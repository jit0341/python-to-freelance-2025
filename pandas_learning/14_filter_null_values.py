import pandas as pd
import numpy as np

data_df = pd.DataFrame({
    'Name': ['Amit','Ravi','None','Mohan'],
    'Age': [25,None,30,28]
    })
print("-----Original Data-----")
print(data_df)

# Filter: Remove rows with any null
clean_data = data_df.dropna()
print("\n----Clean Data(no null)----")
print(clean_data)

