import pandas as pd
df = pd.DataFrame({
    'Value': [30,10,20]},index =[2,0,1])
print("----Original Data-----")
print(df)

# Sort by index
sorted_df = df.sort_index()
print("\n---Sorted by Index-----")
print(sorted_df)


