import pandas as pd
names_df = pd.DataFrame({
    'Name': ['Amit','Anil','Ravi','Ashok','Mohan'],
    })
print("-----Original Data-------")
print(names_df)

# Filter: Names starting wuth 'A'
a_names = names_df[names_df['Name'].str.startswith('A')]
print("\n----Names starting witth 'A'-----")
print(a_names)







