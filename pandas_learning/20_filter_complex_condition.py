import pandas as pd
employee_df = pd.DataFrame({
    'Name': ['Amit','Ravi','Mohan','Sunita'],
    'Department': ['IT','HR','IT','Sales'],
    'Salary': [60000,45000,55000,70000],
    'Experience': [5,2,8,4]
    })
print("-----Original Data------")
print(employee_df)

# Filter: IT Dept, Salary >55k, experience >3
it_senior = employee_df[(employee_df['Department'] =='IT') & (employee_df['Salary'] >= 55000) & (employee_df['Experience'] > 3)]
print("\n----IT Senior Employee-----")
print(it_senior)


