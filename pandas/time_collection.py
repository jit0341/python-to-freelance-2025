import pandas as pd
date = pd.Timestamp('2025-11-21')

print(date.strftime('%B'))  # November (Full month name)
print(date.strftime('%b'))  # Nov (Short month name)
print(date.strftime('%m'))  # 11 (Month number)

print(date.strftime('%d'))  # 21 (Day)
print(date.strftime('%Y'))  # 2025 (4-digit year)
print(date.strftime('%y'))  # 25 (2-digit year)

print(date.strftime('%A'))  # Friday (Full weekday)
print(date.strftime('%a'))  # Fri (Short weekday)

#  Combined formats
print(date.strftime('%d-%m-%Y'))     # 21-11-2025
print(date.strftime('%B %d, %Y'))    # November 21, 2025
print(date.strftime('%d/%m/%y'))     # 21/11/25


