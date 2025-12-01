import pandas as pd
# Employee Sales Data
data = {
    'Employee': ['Alice','Bob','Alice','Charlie','Bob','Alice'],
    'Region': ['East','West','East','South','West','North'],
    'Sales_Amount': [1200,850,1500,400,1100,1900],
    'Years_of_Service': [3,1,3,5,1,3]
    }

# Create the dataFrame
df = pd.DataFrame(data)
print(df)

print("\nPreview (First five rows):")
print(df.head())
"""Select a Column: df['column']
#This selects a single column, returning a Pandas Series object."""
print("\n3. Selecting the 'Sales_Amount'column:")
print(df['Sales_Amount'])
print("\n Selecting the 'Employee'column:")
print(df['Employee'])

""". Filter Rows (Boolean Indexing): df[df['col'] > value]
​This is the most powerful way to filter data based on a condition (or multiple conditions). Here, we find all employees with sales greater than $1000."""
high_sales_filter = df['Sales_Amount'] >1000
low_sales_filter = df['Sales_Amount']< 1000
low_sales_df = df[low_sales_filter]
high_sales_df = df[high_sales_filter]
print("\n4. Filtering(Sales_Amount >1000):")
print(high_sales_df)
print(low_sales_df)

total_sales = df['Sales_Amount'].sum()
print(f"\nTotal sales amount: ${total_sales}")

average = df['Sales_Amount'].mean()
print(f"\nAverage: {average}")

maximum = df['Sales_Amount'].max()
print(f"\nMaximum: {maximum}")

minimum = df['Sales_Amount'].min()
print(f"\nMinimum: {minimum}")

total = df['Sales_Amount'].count()
print(f"\nTotal : {total}")

# 6. Group Data: df.groupby('col')
employee_performance = df.groupby('Employee')['Sales_Amount'].mean()
print("\n6. Grouping(Average Sales by Employee).")
print(employee_performance)

# Sort by 'Sales_Amount' in descending order
df_sorted = df.sort_values('Sales_Amount', ascending = False)
print("\n7(1). Sorting(By Sales Amount in descending).")
print(df_sorted)

# Sort by 'Sales_Amount' in Ascending order
df_sorted = df.sort_values('Sales_Amount', ascending=True)

print("\n7(2). Sorting (By Sales_Amount, Ascending):")
print(df_sorted)

# Add a 'Bonus_Eligible' column: True if
Sales_Amount > 1400 

