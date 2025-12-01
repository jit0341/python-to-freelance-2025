import pandas as pd

data = {
        'Name': ['Govinda Sahu','Bala','Nukesh Rajwade','Rami Yadav','Kariman','Ravi Kumar','Vikas Rao','Vijay Sonwani','Siyaram Sahu'],
        'Amount': [1500,1000,1500,1500,1000,2000,2000,1000,2000],
        'Status': ['Pending','Pending','Pending','Pending','Pending','Pending','Paid','Pending','Pending']
        }

df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)

print("\nFirst 3 rows")
print(df.head(3))

print("\nLast 2 rows")
print(df.tail(2))

print("\nDataFrame info")
print(df.info())

print("\nColumn Names")
print(df.columns)

print("\nDataFrame Shape:")
print(df.shape) # rows, columns

# Practice 2
print("\n=====Practice 2=========")

import pandas as pd
data2 = {
    'Name': ['Ravishankar Singh','Mohammad Irfan','Dhansoo Ram Prajapati"','Suraj Panika','Ashok Kumar Sahu','Shivshankar Yadav'],
    'Area': ['Devnagar','Devnagar','Devnagar','Devnagar','Devnagar','Premnagar',],
    'Village': ['Gram Devnagar','Kalyanpur Schoolpara','Devnagar Kumharpara','Devnagar Panikapara','Gram Kalyanpur','Gram Shyampur Premnagar'],
    'Cases': ['Accident','Accident','Accident','Accident','Accident','Accident']
    }

df2 = pd.DataFrame(data2)
print("\nFull DataFrame:")
print(df2)

print("\nFirst 2 Rows:")
print(df2.head(2))

print("\nLast 3 Rows:")
print(df2.tail(3))

print("\nDataFrame Info:")
print(df2.info())

print("\nColumns Nmae:")
print(df2.columns)

print("\nDataFrame shape:")
print(df2.shape)

# Practice 3
print("\n=========Practice 3===========")
import pandas as pd

data3 = {
    'Name': ['Pushpa Gupta','Shivshankar Jaiswal','Ram Kumar Kanediya'],
    'Village': ['Khadpara Jhilmili','Shivnandanpur','Kusmusi Harijanpara'],
    'Cases': ['Accident','Accident','Accident']
    }
print("\nFull DataFrame:")
df3 = pd.DataFrame(data3)

print("\nFirst 3 Rows")
print(df3.head(3))

print("\nLast 3 Rows")
print(df3.tail(3))

print("\nAll Columns")
print(df3.columns)














