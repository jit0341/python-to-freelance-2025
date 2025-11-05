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



