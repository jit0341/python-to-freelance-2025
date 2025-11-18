import pandas as pd
import numpy as np
from datetime import datetime as dt

#  LAW OFFICE MANAGEMENT SYSTEM
# Uses ALL pandas concepts you've learned!
# ==========================================

print("="*44)
print(" 🏛️\U0001F5A5 LAW OFFICE MANAGEMENT SYSTEM")
print("="*44)

#  1. CLIENT DATABASE (Uses: DataFrame creation, date_range)
np.random.seed(42)
clients_data = {
    'Client_ID': range(1,21),
    'Name': ['Govinda Sahu', 'Nukesh Rajwade', 'Rami Yadav', 'Kariman Rajwade',
             'Ravi Kumar', 'Vikas Rao', 'Vijay Sonwani', 'Siyaram Sahu',
             'Deepak Kumar', 'Pushpa Gupta', 'Shivshankar Jaiswal', 'Ram Kumar',
             'Ravishankar Singh', 'Mohammad Irfan', 'Dhansoo Ram', 'Suraj Panika',
             'Ashok Kumar', 'Shivshankar Yadav', 'Bala', 'Kamal Singh'],
    'Case_Type': np.random.choice(['Accident', 'Dispute', 'Criminal', 'Civil'], 20),
    'Registration_Date': pd.date_range('2025-01-01', periods=20, freq='3D'),
    'Area': np.random.choice(['Surajpur', 'Devnagar', 'Bishrampur', 'Premnagar'], 20),
    'Status': np.random.choice(['Viable', 'Has Lawyer', 'Pending', 'Deceased'], 20),
    'Fee_Amount': np.random.randint(1000, 20000, 20),
    'Payment_Status': np.random.choice(['Paid', 'Pending', 'Partial'], 20),
    'Mobile': [f'9{np.random.randint(100000000, 999999999)}' for _ in range(20)]
}

df_clients = pd.DataFrame(clients_data)


# Calculate additional columns
df_clients['Days_Since_Registration'] = {
(pd.Timestamp.now().normalize () -
df_clients['Registration_Date'].dt.days)}
df_clients['Priority'] = 

df_clients['Days_Since_Registration'].apply
(lambda x: 'High' if x >30 else 'Medium' if x>15 else 'Low')
  # ============================================
# SECTION 1: DATA INSPECTION (head, tail, info, shape)
# ============================================
print("\nSection 1 CLIENT DATABASE OVERVIEW")
print("="*44)
print("\n \u2705 First 5 clients:")
print(df_clients.head())
print("\n \u2705 Last 3 clinte:")
print(df_clients.tail(3))

print("\n \u2705 DataFrame info.")
print(df_clients.info())

print(f"\n \u2705 Total Record:
{df_clients.shape[0] rows ,
{df_clients.shape[1] columns")



