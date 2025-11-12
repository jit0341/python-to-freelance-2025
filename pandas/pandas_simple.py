import pandas as pd

data = {
    'Name': ['Govinda Sahu','Nukesh Rajwade','Rami Yadav','Kariman Rajwade','Ravi Kumar','Vikas Rao','Vijay Sonwani','Deepak Kumar Devangan'],
    'Amount': [2000,1000,1500,1000,1000,100,1000,10000]
    }


df = pd.DataFrame(data)

# Statistics

print("DataFrame")
print(df)

print("\nTotal Amount:")
print(df['Amount'].sum()) # add all amounts

print("\nAverage Amount:")
print(df['Amount'].mean()) # Average

print("\nMaximum Amount:")
print(df['Amount'].max()) # Highest

print("\nMinimum Amount:")
print(df['Amount'].min()) # Lowest

print("\nCounting:")
print(df['Amount'].count()) # How many records

import pandas as pd

# Create insurance claims data
data = {
    'Client_Name': ['Ramesh Kumar', 'Priya Sharma', 'Amit Patel', 'Sunita Devi', 'Rajesh Singh'],
    'Claim_Amount': [50000, 25000, 75000, 15000, 100000],
    'Status': ['Approved', 'Rejected', 'Approved', 'Pending', 'Approved']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print("Insurance Claims Data:")
print(df)
print("\n")

# Calculate statistics
print("Total Claims Amount:", df['Claim_Amount'].sum())
print("Average Claim Amount:", df['Claim_Amount'].mean())
print("Highest Claim:", df['Claim_Amount'].max())
print("Lowest Claim:", df['Claim_Amount'].min())
print("Number of Claims:", df['Claim_Amount'].count())



