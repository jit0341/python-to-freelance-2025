import pandas as pd
# Create 10 dates starting from January 1, 2025
dates = pd.date_range('2025-01-01', periods = 10)
print(dates)

# Create 5 dates, 1 week apart
weekly_dates = pd.date_range('2025-01-01', periods = 5, freq= 'W')
print(weekly_dates)

# Creates 6 dates, 1 month apart
monthly_dates = pd.date_range('2025-01-01', periods = 6, freq = 'ME')
print(monthly_dates)

# Exercise 1: Create 7 dates starting from today (any date you choose), daily
dates = pd.date_range('2025-11-16', periods = 7, freq = 'D')
print(dates)

# Create 4 dates, 1 month apart
month_dates = pd.date_range('2025-11-16', periods = 4, freq= 'MS')
print(month_dates)

# Exercise 3: Create 12 dates (one for each month of 2025)
monthly_dates= pd.date_range('2025-01-01', periods= 12, freq= 'ME')
print(monthly_dates)

