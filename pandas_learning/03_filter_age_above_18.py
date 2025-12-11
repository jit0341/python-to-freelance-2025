import pandas as pd
people_df = pd.DataFrame({
    'Name': ['Amit','Ravi','Priya','Mohan','Sita'],
    'Age': [25,17,30,16,22]
    })
print("---Original Data----")
print(people_df)

# Filter: Age >= 18
adult = people_df[people_df['Age'] >= 18]
print("\n---Adults (Age >= 18)-----")
print(adult)

