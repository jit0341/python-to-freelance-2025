import pandas as pd
names_df = pd.DataFrame({
    'Name': ['Amit','Jitendra','Ravi','Sunita','Mo']
    })
print("-----Original Data-----")
print(names_df)

# Filter: Name length > 5
long_names = names_df[names_df['Name'].str.len() > 5]
print("\n---Name length > 5------")
print(long_names)

