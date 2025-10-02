students = {
        "ST001":{"Name":"Ravi","Age":20,"Course":"Python"},
        "ST002":{"Name":"Prakash","Age":19,"Course":"SQL"},
        "ST003":{"Name":"Atish","Age":18,"Course":"Webdev"}
  }

for student_id,details in students.items():
    print(f"{student_id}: {details['Name']}, Age {details['Age']}")
search_id = input("Enter Student ID:")
if search_id in students:
    student = students[search_id]
    print(f"Name:{student['Name']}")
    print(f"Age:{student['Age']}")
    print(f"Course:{student['Course']}")
else:
    print("Student not found")


