import pandas as pd

# Create Test data
df = pd.DataFrame({
    'Name': ['Ram','Sita','Mohan','Radha','Krishna'],
    'Age': [20,30,20,35,28],
    'Salary': [30000,50000,25000,60000,40000]
    })
# Example 1: AND Condition
print("Young AND High earners (Age <30 AND Salary >35000):")
young_high = df[(df['Age'] <30) & (df['Salary'] >35000)]
print(young_high)

# Example 2: OR Condition
print("\nSenior OR Rich (Age >30 OR Salary >50000):")
senior_rich = df[(df['Age'] >30) | (df['Salary'] >50000)]
print(senior_rich)

# Example 3: Complex Condition
print("\nExperienced Middle earners (Age 25-32 AND Salary 30000-50000):")
target = df[(df['Age'] >= 25) & (df['Age'] <= 32) & (df['Salary'] >= 30000) & (df['Salary'] <= 50000)]
print(target)

df = pd.DataFrame({
    'Name': ['Sneha','Sakshi','Ansh','Ritika','Arya'],
    'Age': [25,20,28,26,35],
    'Salary': [35000,40000,50000,60000,30000]
    })

# Example 1.1: AND condition
print("Young and High earners (Age <30 AND Salary > 35000):")
young_high = df[(df['Age'] < 30) & (df['Salary'] >= 35000)]
print(young_high)

# Example 2.1: OR condition
print("\nSenior OR Rich (Age >30 OR Salary >50000):")
senior_rich = df[(df['Age'] >30) | (df['Salary'] >50000)]
print(senior_rich)

# Example 3.1: Complex conditiom
print("\nExperienced Middle Earners (Age 25-32 AND Salary 30000-50000):")

target = df[(df['Age'] >= 25) & (df['Age'] <= 32) & (df['Salary'] >= 30000) & (df['Salary'] <= 50000)]
print(target)
        
