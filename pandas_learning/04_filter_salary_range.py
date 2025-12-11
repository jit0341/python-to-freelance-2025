import pandas as pd
employee_df = pd.DataFrame({
    'Name': ['Jitendra','Ravi','Mohit','Sunita'],
    'Salary': [45000,60000,35000,80000]
    })
print("-----Original Data--------")
print(employee_df)

# Filter: Salary between 40k-70k
mid_range = employee_df[(employee_df['Salary'] >= 40000) & (employee_df['Salary'] <= 70000)]
print("\n----Salary 40k-70k----+")
print(mid_range)


