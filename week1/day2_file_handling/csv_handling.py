import csv

print("=" *50)
print("CSV Handling")
print("-" *50)

#1. Create CSV file with student data
print("\n1.Ceating CSV file....")
students = [
    ["Id","Name","Course","Marks"],
    ["ST001","Amit","Python",85],
    ["ST002","Sneha","Webdev",88],
    ["ST003","Jitendra","SQL",80]
    ]
with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)
    writer.writerows(students)
print("students.csv created")

# 2. Read csv files
print("\nReading CSV files....")
with open("students.csv","r") as file:
          reader = csv.reader(file)
          for row in reader:
              print(row)

#3. Read as dictionary
print("\n3.Reading as Dictionary....")
with open("students.csv","r") as file:
          reader = csv.DictReader(file)
          for row in reader:
              print(f"{row['Name']} scored {row['Marks']} in {row["Course"]}")







