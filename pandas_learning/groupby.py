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

# Example 1.1 Total Revenue by Region
print("\n---1.1:Total Revenue by Region----")
revenue_by_region = sales_df.groupby('Region')['Revenue'].sum()
print(revenue_by_region)

# Example 1.2: Count of Records/Products by Region

print("\n----1.2: Count of Products by Region---")
count_by_region = sales_df.groupby('Region')['Product'].count()
print(count_by_region)

# Example 2.1: Mean and Max value
# Test Data :Employee Performance Data
employee_df = pd.DataFrame({
    'Department': ['IT','HR', 'IT','Sales','HR','Sales'],
    'Experience': [5,10,2,8,3,15],
    'Salary': [60000,85000,45000,90000,50000,120000],
    'Rating': [4.5,4.0,3.5,4.8,4.2,4.9]
    })
print("\n------Original Employee Data------")
print(employee_df)

# Example 2.1: Average Salary by Department
print("\n----2.1:Average Salary by Department----")
avg_salary = employee_df.groupby('Department')['Salary'].mean()
print(avg_salary.round(2)) # Rounding ro 2 decimal places 

# Example 2.2: Max Experience by Department
print("\n-----2.2: Max Experience by Department----")
max_exp = employee_df.groupby('Department')['Experience'].max()
print(max_exp)

# Grouping by Multiple Columns
# Test Data: Transactiom Data
txn_df = pd.DataFrame({
    'Store': ['A','B','A','C','B','C'],
    'Month': ['Jan','Jan','Feb','Feb','Jan','Mar'],
    'Amount': [200,350,400,150,500,700]
    })
print("\n-----Original Transaction Data----")
print(txn_df)

# Example 3.1: Total Amount by Store AND  month
print("\n-----Total Amount by Store and Month-----")
monthly_sales = txn_df.groupby(['Store','Month'])['Amount'].sum()
print(monthly_sales)

# Example 3.2: Reset DataFrame after grouping
# reset_index
print("\n-----3.2:Reseting the index----")
df_report = txn_df.groupby(['Store','Month'])['Amount'].sum().reset_index()
print(df_report)

# Use Agg Function
# Sum, mean, max 
# Using the Sales Data(sales_df)
print("\n---3.3: Multiple Aggregate on Sales Data-----")
# Revenue column par Sum,mean,count teeno ko ek sath lagu karna
multi_agg = sales_df.groupby('Region').agg(
Total_revenue = ('Revenue','sum'),
Average_Units = ('Units','mean'),
Total_transaction = ('Revenue','count')
)

print(multi_agg)






