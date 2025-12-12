import pandas as pd
sales_df = pd.DataFrame({
    'Product': ['TV','Mobile','Laptop','Fridge','Tablet'],
    'Revenue': [200000,150000,300000,180000,120000]
    })
print("-----Original Data-----")
print(sales_df)

# Filter: Top 3 by Revenue
top_3 = sales_df.nlargest(3,'Revenue')
print("\n----Top 3 Revenue Product-----")
print(top_3)

