import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['North','South','North','East','West'],
    'Revenue': [200000,150000,180000,90000,220000]
    })
print("----Original Data-------")
print(sales_df)
# Filter: North Region AND Revenue > 150k
north_high = sales_df[(sales_df['Region'] =='North') & (sales_df['Revenue'] >150000)]
print("\n----North + High Revenue-----")
print(north_high)

