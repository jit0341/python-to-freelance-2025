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

# Age Classification 2
df1 = pd.DataFrame({'Age': [15,25,35,45,12,21,67]})
df1['Type'] = df1['Age'].apply(lambda x: 'Adult' if x >=18 else 'Child')
print("\nExample 1.1:")
print(df1)

# Price Classification 2
df2 = pd.DataFrame({'Price': [200,1200,3000,300,1500,150]})
df2['Category'] = df2['Price'].apply(lambda x: 'High' if x >=1000 else 'Low')
print("\nExample 2.1:")
print(df2)

# Score Classification 2
df3 = pd.DataFrame({'Score': [40,50,35,60,20]})
df3['Result'] = df3['Score'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print("\nExample 3.1:")
print(df3)

# Stock Classification 2
df4= pd.DataFrame({'Stock': [100,30,1000,0,250]})
df4['Status'] = df4['Stock'].apply(lambda x: 'Available' if x >0 else 'Out')
print("\nExample 4.1:")
print(df4)

# Temperature Classificatiom 2
df5 = pd.DataFrame({'Temp': [30,10,25,40,33]})
df5['Weather'] = df5['Temp'].apply(lambda x: 'Hot' if x >25 else 'Cold')
print("\nExample 5.1:")
print(df5)


