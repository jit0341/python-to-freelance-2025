import pandas as pd
marks_df = pd.DataFrame({
    'Student': ['Ram','Shyam','Geeta','Radha'],
    'Marks': [85,92,78,95]
    })
print("----Original Data-----")
print(marks_df)

# Sort: Highest marks first
top_student = marks_df.sort_values('Marks', ascending = False)
print("\n---Top student first-----")
print(top_student)
