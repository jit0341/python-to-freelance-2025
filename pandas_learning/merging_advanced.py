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


