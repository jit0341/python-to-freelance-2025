import pandas as pd
product_df = pd.DataFrame({
    'Product': ['TV','Mobile','Laptop','Fridge','Tablet'],
    'Category': ['Electronics','Electronics','Electronics','Appliances','Electronics']
    })
print("---Original Data-----")
print(product_df)

# Filter:Only Electronics
electronics = product_df[product_df['Category'] =='Electronics']
print("\n----Electronics only------")
print(electronics)

