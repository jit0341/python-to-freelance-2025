# Exercise 4. File  Handling
print("-" *50)
print("File Handling")
print("-" *50)

#1 write to a file
print("\n1. writing to a file.... ")
file_content = """Name: Jitendra
    Age : 25
    Skills : SQL Python
    Goal : Freelance Developer """

with open("student_info.txt","w")as file:
    file.write(file_content)
    print("File student_info.txt created")

#2 Read from file
print("\n2. Reading from file.... ")
with open("student_info.txt", "r") as file:
   content =  file.read()
   print(content)

#3 Append to a file
print("\n3. Appending to a file.... ")
with open("student_info.txt", "a") as file:
    file.write("\n Status: Learning")
# Read again to see changes
with open("student_info.txt","r") as file:
    print("\nUpdated content")
    print(file.read())


