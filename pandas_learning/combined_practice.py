import pandas as pd

df = pd.DataFrame({
    'Product': ['A','B','C','D','E'],
    'Price': [500,1500,800,2000,300],
    'Stock': [10,25,50,5,100]
    })

# Add category using lambda
df['Price_cat'] = df['Price'].apply(lambda x: 'Premium' if x > 1000 else 'Budget')

# Add stock status using lambda
df['Stock_status'] = df['Stock'].apply(lambda x: 'Low' if x < 20 else 'Good')

# Filter: Premium AND Good stock
premium_good = df[(df['Price_cat'] == 'Premium') & (df['Stock_status'] == 'Good')]

print("All Products:")
print(df)
print("\nPremium products with Good stock:")
print(premium_good)

print("="*42)
import pandas as pd

# 1.Ages
ages = pd.DataFrame({'Age': [15,25,35]})
ages['Type'] = ages['Age'].apply(lambda x: 'Adult' if x >=18 else 'Child')
print (ages)

print("="*42)

# 2. Prices
prices = pd.DataFrame({'Price': [500,1500,800]})
prices['Cat'] = prices['Price'].apply(lambda x: 'High' if x > 1000 else 'Low')
print(prices)

print("="*42)

# 3. Scores
scores = pd.DataFrame({'Score': [35, 85, 55]})
scores['Result'] = scores['Score'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print(scores)

print("="*42)


import pandas as pd

# 1. Create the DataFrame
orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'Amount': [55.50, 120.99, 85.00, 210.25, 45.75]
})

# 2. Add the conditional column ('Order_Size')

# Logic: 'Large' if Amount > 100, else 'Small'
orders['Order_Size'] = orders['Amount'].apply(lambda x: 'Large' if x > 100 else 'Small'
)

# 3. Print the result
print("\n--- Order Size Classification ---")
print(orders)

import pandas as pd

# 1. Create the DataFrame
employees = pd.DataFrame({
    'EmployeeID': [2001, 2002, 2003, 2004],
    'YearsService': [3, 12, 1, 7]
})

# 2. Add the conditional column ('Seniority')
# Logic: 'Senior' if YearsService >= 5, else 'Junior'
employees['Seniority'] = employees['YearsService'].apply(lambda x: 'Senior' if x >= 5 else 'Junior'
)

# 3. Print the result
print("\n--- Employee Seniority Status ---")
print(employees)

import pandas as pd

# 1. Create the DataFrame
sales = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [95, 78, 62, 90, 81]
})

# 2. Add the conditional column ('Performance')
# Logic: 
# - 'Excellent' if Score >= 90
# - 'Good' if Score >= 70 (but less than 90)
# - 'Needs Improvement' if Score < 70

sales['Performance'] = sales['Score'].apply(lambda x: 'Excellent' if x >= 90 
             else ('Good' if x >= 70 
             else 'Needs Improvement')
)

# 3. Print the result
print("\n--- Sales Performance Rating ---")
print(sales)


