import pandas as pd
data_df = pd.DataFrame({
    'Name': ['Amit','Ravi','Amit','Mohan','Ravi']
    })
print("----Original Data------")
print(data_df)

# Filter: Remove Duplicates
unique_names = data_df.drop_duplicates()
print("\n---Unique Names-----")
print(unique_names)

