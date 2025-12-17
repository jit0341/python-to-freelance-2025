import pandas as pd
# Imner Merge
students = pd.DataFrame({
    "roll": [1,2,3,4,5],
    "name": ["Aman","Riya","Sohan","Neha","Ravi"]
    })
print("----Students Data-----")
print(students)

marks = pd.DataFrame({
    "roll": [1,2,4,5,6],
    "maths": [78,98,66,80,75]
    })
print("\n----Marks Data----")
print(marks)

result_inner = pd.merge(students,marks, on = "roll", how = "inner")
print("\n---Merged data Inner----")
print(result_inner)

# Left  merge
result_left = pd.merge(students,marks, on = "roll", how = "left")
print("\n---Merged data Left----")
print(result_left)

# Right Merge
result_right = pd.merge(students,marks, on = "roll", how = "right")
print("\n---Merged data Right-----")
print(result_right)

# Outer Merge
result_outer = pd.merge(students,marks, on= "roll", how = "outer")
print("\n---Merged data Outer-----")
print(result_outer)

# Example 2
print("\n----Example 2-------")
employees = pd.DataFrame({
    "EmpID": [101,102,103],
    "DeptCode": ["D1","D2","D3"]
    })
print("\n----Employees Data----")
print(employees)
departments = pd.DataFrame({
    "Code": ["D1","D2","D4"],
    "DeptName": ["Sales","HR","Marketing"]
    })
print("\n----Departments Data----+")
print(departments)

emp_dept = pd.merge(employees, departments, left_on = "DeptCode", right_on = "Code", how = "left")
print(emp_dept)

# Example 3
print"\n--------Example 3-----------")

