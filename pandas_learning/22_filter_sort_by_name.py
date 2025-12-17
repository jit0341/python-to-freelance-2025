import pandas as pd
data_df = pd.DataFrame({
    'Name': ['Ravi','Mohan','Aditya','Kapoor','Tinku'],
    'Salary': [40000,50000,60000,35000,65000]
    })
print("---Original Data------")
print(data_df)

# Filter: Sorted by Name
names_df = data_df.sort_values('Name')
print("\n-----Sorted by name-----")
print(names_df)
