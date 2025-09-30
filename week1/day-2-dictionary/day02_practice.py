print("=" * 50)
print("Day 2 - Dictionary & File Handling")
print("=" * 50)

print("\nExercise 1: Student Database")
print("-" * 50)
# Create a dictionary for one student
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Pythin" ,
    "marks": 85 
    }
#Print the dictionary
print(student)
# Access and print individual values
print(f"Student Name: {student['name']}")
print(f"Marks: {student['marks']}")

# Add a new key
student["city"] = "Rewa"
print(f"\nAfter adding cuty: {student}")
 # Modify existing value
student["marks"] = 90
print(f"Updated marks: {student['marks']}")

# Exercise 2 Safe Dictiinary Access
print(f"\n\nExercise 2 Safe Dictionary Access")
print("-" * 50)
student = {
  "name": "Priya",
  "age": 22,
  "course": "Data Science"
  }
email = student.get("email")
print(f"Email(using.get) : {email}")

# Method 2 
email = student.get("email", "Not provided")

print(f"Email with default: {email}")

if "email" in student:
    print(f"Email{student['email']}")
else:
    print("Email key does not exist")
# Add all key check
print(f"\nAll keys in dictionary: {student.keys()}")
print(f"\nAll values in dictionary: {student.values()}")

# Exercise 3. Student Management System
print("\n\nExercuse 3:  Nested Dictionary")
print("-" * 50)

# Multiple students with nested data
students_db = {
    "ST001": {
        "name": "Amit",
        "age": 21,
        "courses": ["Python", "Data Science"],
        "marks": {"Python": 85, "Data Science": 90}
},
    "ST002": {
        "name": "Sneha",
        "age": 22,
        "courses": ["Webdev", "Python"],
        "marks": {"webdev": 85, "Python": 92}}} 
        
    # Access nested data
print(f"Student ST001 name: {students_db['ST001']['name']}")
print(f"Amit's Python marks: {students_db['ST001']['marks']['Python']}")

# Loop through All Students
print("\nAll Students")
for student_id , details in students_db.items():
    print(f" {student_id}: {details['name']}-Age {details['age']}")

# Calculate average marks for ST001
marks = students_db['ST001']['marks']
average = sum(marks.values()) /len(marks)
print(f"\nAmit's Average: {average}")

# Add third student
students_db['ST003']= { 
        "name": "Jitendra",
        "age": 48,
        "courses": ["SQL", "Python"],
        "marks": {"SQL": 80, "Python": 85}
}

# Print ST003 details
print(f"\nStudent ST003 name: {students_db['ST003']['name']}")
print(f"Student ST003 courses: {students_db['ST003']['courses']}")
print(f"Student ST003 marks: {students_db['ST003']['marks']}")








