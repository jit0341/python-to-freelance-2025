import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['South','North','East','West','North'],
    'Revenue': [200000,160000,300000,180000,150000]
    })
print("-----Original Data-----")
print(sales_df)
# Sort bt region then revenue
sorted_df = sales_df.sort_values(['Region','Revenue'] ,ascending = [True,False])
print("\n----Sorted by region then revenue-----")
print(sorted_df)

