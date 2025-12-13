import pandas as pd
orders_df = pd.DataFrame({
    'Order_ID': [1,2,3,4,5],
    'Date': pd.to_datetime(['2024-01-05','2024-01-15','2024-01-25','2024-02-05','2025-02-15'])
    })

print("------Original Data-------")
print(orders_df)

# Filter:January Orders
jan_orders = orders_df[orders_df['Date'].dt.month ==1]
print("\n---January Orders-----")
print(jan_orders)

feb_orders = orders_df[orders_df['Date'].dt.month == 2]
print("\n-----February Orders-----")
print(feb_orders)


