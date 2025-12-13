import pandas as pd
products_df  = pd.DataFrame({
    'Product': ['Apple iphone','Samsung mobile','Apple Watch','Dell Laptop']
    })
print("----Original Data-------")
print(products_df)

# Filtet: contains 'Apple'
apple_product = products_df[products_df['Product'].str.contains('Apple')]
print("\n---Apple Products-----")
print(apple_product)


