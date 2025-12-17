import pandas as pd
sales_df = pd.DataFrame({
    'Product': ['TV','Mobile','Laptop','Fridge'],
    'Revenue': [200000,150000,300000,180000]
    })
print("----Original Data-------")
print(sales_df)

# Filter: By revenue (descending)
sorted_df = sales_df.sort_values('Revenue', ascending = False)
print("\n-----Sorted by revenue----")
print(sorted_df)


