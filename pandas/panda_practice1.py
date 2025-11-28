# Month Extraction
import pandas as pd

dates = pd.date_range('2025-01-01', periods = 5, freq = '15D')
print("Original Dates:")
print(dates)

# Month Names
months = dates.strftime('%B')
print("\nMonth names:")
print(months)

#Use in Dataframe
test_df = pd.DataFrame({
    'Date': dates,
    'Amount': [1000,2000,1500,3000,2500]
    })
test_df['Month'] = test_df['Date'].dt.strftime('%B')
print("\nDataFrame:")
print(test_df)
