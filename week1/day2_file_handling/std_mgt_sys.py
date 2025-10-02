import csv
student_data = {

        "ST001":{"Name":"Ravi","Age":20,"Course":"Python"},
        "ST002":{"Name":"Prakash","Age":19,"Course":"SQL"},
        "ST003":{"Name":"Atish","Age":18,"Course":"Webdev"},
        "ST004":{"Name":"Sunil","Age":21,"Course":"Java"},
        "ST005":{"Name":"Yogesh","Age":22,"Coursr":"HTML"}

        }
print(student_data)

with open("student_data.csv","w") as file:
    writer = csv.writer(file)
    writer. writerows(student_data)

with open("student_data.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("student_data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} {row['Age']} {row['Course']}")

