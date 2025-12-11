import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['North','South','North','East','South'],
    'Product': ['TV','Mobile','Laptop','TV','Laptop']
    })
print("----Original Data---------")
print(sales_df)

# Filter: Only North region
north_sales = sales_df[sales_df['Region'] == 'North']
print("\n---North region sales-----")
print(north_sales)
