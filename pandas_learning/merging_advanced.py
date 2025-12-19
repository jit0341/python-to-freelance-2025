# Exercise 1: Multiple Conditions
# Merge on two columns
import pandas as pd
students = pd.DataFrame({
    "roll": [1,2,3,1,2],
    "class": ["A","A","B","B","B"],
    "name": ["Amit","Priya","Rahul","Neha","Ravi"]
    })
print("-----Students Data-----")
print(students)

marks = pd.DataFrame({
    'roll': [1,2,3,1,2],
    'class': ['A','A','B','B','B'],
    'subject': ['Maths','Maths','Maths','Science','Science'],
    'marks': [85,90,78,92,88]
    })
print("\n-----Marks Data--------")
print(marks)

result = pd.merge(students,marks,on=['roll','class'])
print("\n----Merged result-----")

print(result)

# Exercise 2: Handling Duplicates
# suffixes for same column names
sales1 = pd.DataFrame({
    'id': [1,2,3],
    'amount': [100,200,300],
    'date': ['2024-01','2024-01','2024-02']
    })
print("\n----Sales1 Data------")
print(sales1)

sales2 = pd.DataFrame({
    'id': [1,2,4],
    'amount': [150,250,400],
    'date': ['2024-02','2024-02','2024-03']
    })
print("\n----Sales2 Data------")
print(sales2)

result = pd.merge(sales1,sales2, on = 'id', suffixes = ('_jan','_feb'))
print("\n-----Merged Result------")
print(result)

# Exercise 3: Indicator Column
# Track merge source
import pandas as pd
df1 = pd.DataFrame({
    'id': [1,2,3], 
    'name': ['A','B','C']})
print("----df1 data-----")
print(df1)
df2 = pd.DataFrame({
    'id': [2,3,4],
    'age':[25,30,35]})
print("\n-----df2-----")
print(df2)
result = pd.merge(df1,df2,on = 'id', how = 'outer', indicator = True)
print(result)
# Shows: left_only, right_only, both
print(result['_merge'].value_counts())

# Exercise 4: Index-based Merge
# Using index instead of column
df1 = pd.DataFrame({
    'name': ['Amit','Priya','Rahul'],
    'index': [101,102,103]
    })
print("\n----df1 Data------")
print(df1)

df2 = pd.DataFrame({
    'salary': [50000,60000,55000],
    'index': [101,102,104]
    })
print("\n----df2 Data-------")
print(df2)

result = pd.merge(df1,df2, left_index = True, right_index = True, how = 'outer')
print(result)

# Exercise 5: Concat vs Merge
# Vertical stacking (concat)
jan_sales = pd.DataFrame({
    'product':['A','B'],
    'qty':[19,20]
    })
print("---jan_sales data----")
print(jan_sales)

feb_sales = pd.DataFrame({
    'product':['C','D'],
    'qty':[15,25]
    })
print("\n----feb_sales data----")
print(feb_sales)

all_sales = pd.concat([jan_sales,feb_sales], ignore_index = True)
print("\nConcatenated:")
print(all_sales)
# Horizontal Merging
prices = pd.DataFrame({
    'product':['A','B','C','D'],
    'price':[100,200,150,250]
    })
print("\n---Prices data------")
print(prices)

result = pd.merge(all_sales,prices,on = 'product')
print("\nMerged:")
print(result)

# Exercise 6: Real Business case: Order
#Analysis
# Customers
customers = pd.DataFrame({
    'cust_id':[1,2,3,4],
    'name':['Amit','Priya','Rahul','Neha'],
    'city':['Delhi','Mumbai','Bangalore','Delhi']
    })
print("\n---Customers Data---")
print(customers)
# Orders
orders = pd.DataFrame({
    'order_id':[101,102,103,104,105],
    'cust_id':[1,2,1,3,1],
    'amount':[500,800,1200,600,900]
    })
print("\n----Orders data----")
print(orders)

# Products
products = pd.DataFrame({
    'order_id':[101,102,103,104,105],
    'product':['Laptop','Phone','Tablet','Mouse','Keyboard']
    })
print("\n----Products data-----")
print(products)
# Analysis: Customers+Orders+Products
step1 = pd.merge(customers,orders,on = 'cust_id')
full_data = pd.merge(step1,products, on = 'order_id')
print("\n---Full Analysis---")
print(full_data)

# Who soent Most
customer_spending = full_data.groupby('name') ['amount'].sum().sort_values(ascending = False)
print("\nTop Spenders:")
print(customer_spending)
# Missing data handling
# Some students have marks some don't.
students = pd.DataFrame({
    'roll':[1,2,3,4,5],
    'name':['A','B','C','D','E']
    })
print("\n---Students Data----")
print(students)
marks = pd.DataFrame({
    'roll':[1,3,5],
    'marks':[85,90,78]
    })
print("\n---Marks data-----")
print(marks)

result = pd.merge(students,marks,on = 'roll', how = 'left')
print("\n--Merged data")
print(result)
# Fill missing marks with 0
result['marks'].fillna(0,inplace = True)
print("\nAfter filling")
print(result)



