Day 2 section:

# Dictionary

## What it is:

1.Dictionaries are unordered collections. It has key-values pair. It is written in curly bracket{ }
2. Lists are ordered collections. It is written in square bracket [ ].

## Structure:
student = {"name": "Raj", "age": 20}

## How to access:
[Write example of accessing and adding to dictionary]
1.For accessing dictionary
print(f"key values:{key['values']}")
print(f"values:{key['values']}")

2. For adding to dictionary
student["key"] = "values"
note: Adding single key and whole new dictionary are same.
3. Modify existing values
student["key"] = "changed values"



## Where I struggled:
[Be honest - what confused you about dictionaries?]

I am confused in safe dictionary access.

# File Handling
1. We write file cintents first in
""" FILE_CONTENT =key:values """

2. writing in a file
with open("file.txt","w") as file:
    file.write(FILE_CONTENT)

3. reading from file
with open("file.txt","r") as file:
    content = file.read( )

4. appending to a file
with ooen("file.txt","a") as file:
    file.write("\n keys:values")

5. read again after appending
with open("file.txt","r") as file:
    print(file.read())
## Basic operations:
[Write examples of read, write, append]

## Why we use "with open":
[Explain in your own words]
we use 'with open' to open and close file automatically.

## CSV files:
[Explain what you learned about CSV]

---
1. In CSV files we first import csv. write content as list. first line we add keys, from second line we add values accordingly.

2. For writing all process is same as in files. We use writer.
    writer = csv.writer(file)
    writer.writerow(content)
note:- writerow is used to arrange comma separated values as column.

3. For reading CSV file
with open.......
   reader = csv.reader(file)
   for row in reader: 
   # it reads all as column.
       print(row)
4. read as dictionary
with open......
    reader = csv.DictReader(file)
    for row in reader
    print(f"{row["name"]} {row]"marks"]} {row["course"]}")

confusion: DictReader and row need to be clear.

# Contact Manager Project

## What I built:
[Describe the features]

## Key concepts used:
- Dictionaries for storing contacts
   like contact { }
- Loops for menu . I used while True: loop for making menu.
- Used conditional if for making choices.
- File read/write for persistence
- Used for loop for writing content in dictionary.
- Used 'with open' to save the contents into a file permanently.
- [etc]

## What I learned from building it:
[Most important - what clicked for you?]
we can create menu based application eben with dictionary, while, if, for and files.

