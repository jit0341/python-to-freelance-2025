import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['South','North','East','West','North','South','East'],
    'Product': ['Oil','Rice','Wheat','Pulsese','Rice','Oil','Wheat'],
    'Revenue': [100000,2000000,3000000,1500000,1800000,800000,2500000],
    'Quantity_in_kilo': [1000,4000,5000,7000,9000,4000,10000]
    })
print("\n---Show all Data------")
print(sales_df)

# Grouo the Data and take Summary
print("\n---Grouping and Summary----")
region_summary = sales_df.groupby('Region')['Revenue'].sum().reset_index()
print(region_summary)

# Sorting in Descending Order
print("\n-----In Descending Order-------")
# ascending = False matlab bade se chhota
sorted_summary = region_summary.sort_values(by= 'Revenue', ascending = False)

print("\n---Regions Ranked by Revenue(Highest to lowest)----")
print(sorted_summary)

sort_summary = region_summary.sort_values(by = 'Revenue', ascending = True)

print("\n----Regions Ranked by Revenue(Lowest to highest)-----")
print(sort_summary)

# Top performing Region 
top_region = sorted_summary.head(1)
print("\n---Top performing region is:-----")
print(top_region)
top3_region = sorted_summary.head(3)
print("\n----Top 3 Performing region:-----")
print(top3_region)

print("\n--------Practice 2--------------------------------------")
import pandas as pd
sales_df = pd.DataFrame({
    'Region': ['South','North','East','West','North','South','East'],
    'Product': ['Oil','Rice','Wheat','Pulsese','Rice','Oil','Wheat'],
    'Revenue': [100000,2000000,3000000,1500000,1800000,800000,2500000],
    'Quantity_in_kilo': [1000,4000,5000,7000,9000,4000,10000]
    })
print("\n---Show all Data------")
print(sales_df)

print("\n----Total Revenue----------")
product_summary = sales_df.groupby('Product')['Revenue'].sum()
print(product_summary)

sorted_summary = product_summary.sort_values(ascending = False)
print("\n----Sorted Cereals(Highest to lowest)-----")
print(sorted_summary)
print("\n-----Top 3 Product-------")

top3_product = sorted_summary.head(3)
print(top3_product)



