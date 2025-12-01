import pandas as pd

# Example 1: Age Classification
df1 = pd.DataFrame({'Age': [15,25,35,10,40]})
df1['Type'] = df1['Age'].apply(lambda x: 'Adult' if x >= 18 else 'Child')
print("Example 1:")
print(df1)

# Example 2: Price Classification
df2 = pd.DataFrame({'Price': [500,1500,800,2000,300]})
df2['Category'] = df2['Price'].apply(lambda x: 'High' if x >= 1000 else 'Low')
print("\nExample 2:")
print(df2)

# Example 3: Score Classification
df3 = pd.DataFrame({'Score': [45,85,30,90,55]})
df3['Result'] = df3['Score'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print("\nExample 3:")
print(df3)

# Example 4: Stock Classification
df4 = pd.DataFrame({'Stock': [5,50,0,100,20]})
df4['Status'] = df4['Stock'].apply(lambda x: 'Available' if x >0 else 'Out')
print("\nExample 4:")
print(df4)

# Example 5: Temperature Classification
df5 = pd.DataFrame({'Temp': [15,30,10,35,25]})
df5['Weather'] = df5['Temp'].apply(lambda x: 'Hot' if x >25 else 'Cold')
print("\nExample 5:")
print(df5)



