import pandas as pd
student_df = pd.DataFrame({
    'Student': ['Ram','Shyam','Geeta','Radha'],
    'Marks': [45,32,67,28]
    })
print("-----Original Data-------")
print(student_df)

# Filter: Marks >= 33(pass)
passed = student_df[student_df['Marks'] >= 33]
print("\n----Passed Students------")
print(passed)
    
