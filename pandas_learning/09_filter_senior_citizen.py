import pandas as pd
citizens_df = pd.DataFrame({
    'Name': ['Ramesh','Suresh','Kamala','Vijay'],
    'Age': [65,45,70,58]
    })
print("-----Original Data-------")
print(citizens_df)

# Filter: Age >= 60
seniors = citizens_df[citizens_df['Age'] >= 60]
print("\n-----Senior Citizen (>=60)----")
print(seniors)

