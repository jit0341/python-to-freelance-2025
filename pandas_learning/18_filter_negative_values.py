import pandas as pd
transactions_df = pd.DataFrame({
    'Transaction': ['T1','T2','T3','T4'],
    'Amount': [500,-200,300,-150]
    })
print("-------Original Data-----")
print(transactions_df)

# Filter: Only Positive Amounts
positive = transactions_df[transactions_df['Amount'] > 0]
print("\n------Positive Transactions-----")
print(positive)


