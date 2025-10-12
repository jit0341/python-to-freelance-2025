import os

def calculate_average(marks):
    """Calculate average of marks"""
    if not marks:
        return 0
    return sum(marks.values())/ len(marks)

def get_grade(average):
    """Convert average to grade"""
    if average >=90:
        return "A"
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"

def add_student(students):
    """Add a new student"""
    try:
        name =input("Enter student name:")

        #Check if student already exists
        if any(s['name'].lower() == name.lower() for s in students):
            print(f"Student {name} already exists!")
            return

        # get marks for 3 subjects
        marks = {}
        subjects = ["Math","English","Science"]

        for subject in subjects:
            try:
                mark = float(input(f"Enter {subject} marks(0-100): "))
                if mark <0 or mark >100:
                    print("Marks must be 0-100!")
                    return
                marks[subject] = mark

            except ValueError:
                print("Invalid input! Please enter a number")
                return

        average = calculate_average(marks)
        grade = get_grade(average)

        student = {
          "name": name,
          "marks": marks,
          "average": average,
          "grade": grade
        }

        students.append(student)
        print(f"Student{name} added successfully! Grade: {grade}")

    except Exception as e:
        print(f"Error adding student : {e} ")

def view_all_students(students):
    """Display all students"""
    if not students:
        print("No students recorded yet!")
        return
    print("\n" + "="*60)
    print("ALL STUDENTS")
    print("="*60)


    for student in students:
        print(f"\nName: {student['mame']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {student['average']:2f}")
        print(f"Grade: {student['grade']}")

def search_student(students):
    """Search for a student by name"""
    name = input("Enter student name to search:")

    #Use list comprehension to find student
    found = [s for s in students if s['name'].lower == name.lower()]
    if found:
        student = found[0]
        print(f"\nName: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {student['average']:2f}")
        print(f"Grade: {student['grade']}")

    else:
        print(f"Student{name} not found")

def top_performers(student):
    """Show top 3 performers using lambda +sorted"""
    if not students:
        print("No students to display!")
        return
    # Sort by average using lambda (highest first)
    sorted_students = sorted(students,key = lambda x:x ['average'], reverse = True)

    print("\n" + "="*60)










        



