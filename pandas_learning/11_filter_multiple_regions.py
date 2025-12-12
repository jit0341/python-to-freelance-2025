import pandas as pd 
# Medium Filtering
sales_df = pd.DataFrame({
    'Region': ['North','South','East','West','North','East'],
    'Revenue': [200000,150000,180000,160000,190000,170000]
    })
print("------Original Data--------")
print(sales_df)

# Filter:North OR East region
ne_region = sales_df[sales_df['Region'].isin(['North','East'])]
print("\n---North & East regions------")
print(ne_region)

