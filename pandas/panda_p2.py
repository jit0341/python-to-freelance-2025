import pandas as pd

clients = {
    'Name': ['Govinda Sahu','Nukesh Rajwade','Rami Yadav','Kariman Rajwade','Ravi Kumar','Vikas Rao','Vijay Sonwani','Siyaram Sahu','Deepak Kumar Devangan'],
    'FIR No.': [581,585,586,587,591,272,597,598,282],
    'Area': ['Surajpur','Surajpur','Surajpur','Surajpur','Surajpur','Bishrampur','Surajpur','Surajpur','Surajpur'],
    'Status': ['Pending','Confirmed','Pending','Pending','Pending','Confirmed','Pending','Pending','Pending'],
    'Amount': [1000,500,1000,1000,1000,5000,1000,1000,20000],
    'Date': [2,4,5,8,8,9,10,11,12]
    }
df = pd.DataFrame(clients)
print("="*44)
print("Client Tracker")
print("="*44)

print(df)

print("\n"+"="*44)
print("Statistics")
print("="*44)

total_clients = len(df)
confirmed = len(df[df['Status'] == 'Confirmed'])

pending = len(df[df['Status'] == 'Pending'])

total_income = df[df['Status'] == 'Confirmed'] ['Amount'].sum()

print(f"Total Clients: {total_clients}")
print(f"Confirmed: {confirmed}")
print(f"Pending: {pending}")
print(f"Total Income: {total_income}")
print(f"Expected Income (if all confirmed): ₹{df['Amount'].sum()}")

# Area wise Summary
print("\n"+"="*44)
print("Area wise summary")
print("="*44)
print(df.groupby('Area')['Status'].value_counts())

print("\nConversion Rate:")
conversion_rate = (confirmed/total_clients)*100
print(f"{conversion_rate:.1f}%")



