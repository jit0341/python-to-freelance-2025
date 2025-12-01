import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

clients = {
    'Client_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    
    'Type': ['Dispute', 'Dispute', 'Dispute', 'Dispute', 'Dispute', 
             'Dispute', 'Dispute', 'Dispute', 'Dispute', 'Dispute', 
             'Dispute', 'Accident', 'Accident', 'Accident', 'Accident', 
             'Accident'],  # Fixed: Now 16 items, removed extras
    
    'Status': ['Viable', 'Viable', 'Viable', 'Viable', 'Viable', 
               'Viable', 'Viable', 'Viable', 'Viable', 'Viable', 
               'Has Lawyer', 'Deceased', 'Has Lawyer', 'Viable', 
               'Has Lawyer', 'Has Lawyer'],  # 16 items (correct!)
    
    'Day': [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6]  # 16 items (correct!)
}

df = pd.DataFrame(clients)
print("=" * 40)
print("6-Day work summary")
print(df.to_string())

print("\n" + "=" * 40)
print("STATISTICS")

total = len(df)
viable = len(df[df['Status'] == 'Viable'])
has_lawyer = len(df[df['Status'] == 'Has Lawyer'])
deceased = len(df[df['Status'] == 'Deceased'])

print(f"Total Cases Found: {total}")
print(f"Viable Cases: {viable} ({viable/total*100:.1f}%)")
print(f"Already Has Lawyer: {has_lawyer} ({has_lawyer/total*100:.1f}%)")
print(f"Deceased: {deceased} ({deceased/total*100:.1f}%)")

print("\n" + "=" * 40)
print("TYPE BREAKDOWN")
print("=" * 40)
print(df['Type'].value_counts())

print("\n" + "=" * 40)
print("DAILY PROGRESS")
print("=" * 40)
print(df.groupby('Day')['Status'].value_counts())






