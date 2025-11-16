import pandas as pd

data = {
    'Name': ['Rahul','Priya','Amit'],
    'City': ['Delhi','Mumbai','Kolata'],
    'Age': [25,19,34],
    'Income': [50000,60000,55000]
    }
df = pd.DataFrame(data)

# get ome column
print("\nNames only")
print(df['Name'])

print("\nIncomes only")
print(df['Income'])

# Get Multiple Columns
print("\nName and City")
print(df[['Name','City']])

print("\nName,City and Income")
print(df[['Name','City','Income']])




