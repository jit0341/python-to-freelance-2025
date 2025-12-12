import pandas as pd
items_df = pd.DataFrame({
    'Item': ['Rice','Oil','Sugar','Ghee'],
    'Price': [50,120,45,450]
    })
print("-----Original Data------")
print(items_df)

# Filter:Price > 100
expensive = items_df[items_df['Price'] > 100]
print("\n----Expensive Items------")
print(expensive)

