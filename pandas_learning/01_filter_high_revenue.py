import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['North','South','North','East','South'],
    'Revenue': [200000,150000,120000,160000,200000]
    })
print("---Original Data-----")
print(sales_df)

# Filter: Revenue >150000
high_revenue = sales_df[sales_df['Revenue'] > 150000]
print("\n----High Revenue (>150k)---")
print(high_revenue)


