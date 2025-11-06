import pandas as pd
# Create data loke dictionary

data1 = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': [25,30,28],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
    }

# Create DataFrame
df = pd.DataFrame(data1)

# Display it.
 
print(df)
print("==========================")

import pandas as pd

data2 = {
    'Name': ['Ravi', 'Ankush', 'Yogesh', 'Prakash', 'Sunil', 'Atish'],
    'Age': [45,40,44,45,43,42],
    'City': ['Satna', 'Raipur', 'Itarsi', 'Bhopal', 'Badodara', 'Indore']
    }

df2 = pd.DataFrame(data2)
print(df2)
print("=========================")

import pandas as pd

student_data = {
        'Name': ['Aahu', 'Pihu', 'Monika', 'Sonakshi', "Kajal", 'Akanksha'],
    'Age': [20,22,23,25,27,14],
    'School': ['Sadhu Ram Vidya Mandir', 'Global Public School', 'Swami Atmanand School', 'DAV Public School', 'Carmel Convent School', 'Saraswati Shishu Mandir']
    }
df_students = pd.DataFrame(student_data)
print(df_students)
print("=" *20)

import pandas as pd

client_data = {
    'Name': ['Sudheer', 'Ravindra', 'Ramchandra'],
    'FIR_No': [64,9,4],
    'Date': ['30/01/25', '04/01/25', '02/01/25'],
    'Status': ['Confirmed', 'Confirmed', 'Pending']
    }

df = pd.DataFrame(client_data)
print(df)
print("=" *35)

import pandas as pd


client_data2 = {
    'Name': ['Govinda Sahu', 'Bala', 'Nukesh Rajwade', 'Rami Yadav', 'Kariman Rajwade', 'Ravi Kumar'],
    'FIR_No': [581,583,585,586,587,591],
    'Mobile_No': [9131472937,9669033832,8839827015,9617168714,6265808207,7697952514],
    'Area': ['Surajpur', 'Surajpur', 'Surajpur', 'Surajpur', 'Surajpur', 'Surajpur'],
    'Village': ['Pampapur Jharpara', 'Manpur Turiyapara', 'Unchdih Jagarnathpara', 'Gram Chopan Beejpara', 'Bharuamuda Khalpara', 'Kusmusi Harijanpara'],
    'Status': ['Confirmed', 'Pending', 'Comfirmed', 'Contacted', 'Confirmed', 'Confirmed']
    }
df = pd.DataFrame(client_data2)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 15)

print(df.to_string())




