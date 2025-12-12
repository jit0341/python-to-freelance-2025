import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['North','South','East','West'],
    'Revenue': [200000,150000,180000,160000]
    })
print("-----Original Data--------")
print(sales_df)

# Filter: Exclude South
not_south = sales_df[sales_df['Region'] !='South']
print("\n---All Except South----")
print(not_south)

