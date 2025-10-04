
# Practising contact manager

contacts = {}
# Load contacts from file if it exists
try:
    with open("contacts.txt","r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3:
                name, phone, email = parts
                contacts[name] = {"phone": phone, "email": email}
    print(f"Loaded {len(contacts)} contacts from file")
except FileNotFoundError:
    print("No saved contacts found. Starting fresh.")

print("====Contact Manager====")

while True:
    print("====Menu====")
    print("1. Add contact ")
    print("2. View all contacts ")
    print("3. Exit ")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        name = input(" Enter name:-")
        phone = input(" Enter phone number: ")
        email = input(" Enter email:-")
        
        print(f" Name: {name}")
        print(f" phone: {phone}")
        print(f" email: {email}")
        print(f"Contact {name} saved successfully")
        
        contacts[name] = {"email": email, "phone": phone}
        print(f"{name} added to contacts")
    
    elif choice == "2":
        if len(contacts) == 0:
            print("No contact saved yet!")
        else:
            print("\nAll contact")
            for name, details in contacts.items():
                print(f"name: {name}")
                print(f"phone: {details['phone']}")
                print(f"email: {details['email']}")
    
    elif choice == "3":
        with open("contacts.txt","w") as file:
            for name, details in contacts.items():
                line = f"{name}|{details['phone']}|{details['email']}\n"
                file.write(line)
        
        print("contacts saved in a file")
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")



