import pandas as pd
expenses = pd.DataFrame({
    'Date': pd.date_range('2025-01-01', periods = 30, freq = 'D'),
    'Amount': [100,150,200,120,170,220,250,50,75,80,160,260,110,130,190,210,230,240,270,300,280,310,290,320,240,125,225,325,175,275]
    })  # Daily expense
expenses['Month'] = expenses['Date'].dt.strftime('%B')

# Group by Month
monthly_total = expenses.groupby('Month')['Amount'].sum()
print(f"January Total: ₹{monthly_total['January']}")


