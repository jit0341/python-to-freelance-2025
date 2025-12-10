# Basic sum and count
import pandas as pd
# Test Data : Sales Data
sales_df = pd.DataFrame({
    'Region': ['North','South','North','East','South','West','East'],
    'Product': ['TV','Mobile','Laptop','TV','Laptop','Fridge','Mobile'],
    'Revenue': [200000,150000,1200000,160000,200000,180000,1100000],
    'Units': [10,5,12,8,29,9,11]
    })

print("------Original Sales Data--------")

print(sales_df)
