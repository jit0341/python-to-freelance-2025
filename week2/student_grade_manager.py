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
     for i, student in enumerate(sorted_students[:3], 1):
        print(f"{i}. {student['name']} - Average: {student['average']:.2f} (Grade: {student['grade']})")

def view_by_grade(students):
    """Filter students by grade"""
    grade = input("Enter grade to filter (A/B/C/D/F): ").upper()
    
    # Use list comprehension to filter
    filtered = [s for s in students if s['grade'] == grade]
    
    if filtered:
        print(f"\nStudents with grade {grade}:")
        for student in filtered:
            print(f"- {student['name']}: Average {student['average']:.2f}")
    else:
        print(f"No students found with grade {grade}")

def save_students(students):
    """Save students to file"""
    try:
        with open("students.txt", "w") as file:
            for student in students:
                marks_str = "|".join([f"{subject}:{mark}" for subject, mark in student['marks'].items()])
                line = f"{student['name']}|{marks_str}|{student['average']:.2f}|{student['grade']}\n"
                file.write(line)
        print("Students saved to file")
    except Exception as e:
        print(f"Error saving: {e}")

def load_students():
    """Load students from file"""
    students = []
    
    if os.path.exists("students.txt"):
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split("|")
                        if len(parts) >= 4:
                            name = parts[0]
                            # Parse marks
                            marks = {}
                            for i in range(1, len(parts) - 2):
                                subject, mark = parts[i].split(":")
                                marks[subject] = float(mark)
                            
                            average = float(parts[-2])
                            grade = parts[-1]
                            
                            student = {
                                "name": name,
                                "marks": marks,
                                "average": average,
                                "grade": grade
                            }
                            students.append(student)
            
            if students:
                print(f"Loaded {len(students)} students")
        except Exception as e:
            print(f"Error loading: {e}")
    
    return students

def main():
    """Main program loop"""
    students = load_students()
    
    while True:
        print("\n===MENU===")
        print("1. Add student")
        print("2. View all")
        print("3. Search student")
        print("4. Top performers")
        print("5. View by grade")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            top_performers(students)
        elif choice == "5":
            view_by_grade(students)
        elif choice == "6":
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()












        



