# Contact Manager-Day 3 Project
contacts = {}

print("===Contact Manager===")
print("Contacts:", contacts)

while True:
    print("\n---Menu---")
    print("1.Add Contact")
    print("2. View All")
    print("3. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        name = input("Enter Name:")
        phone = input("Enter Phone:")
        email = input("Enter email:")

        contacts[name] = {"phone":phone,"email":email}
        print(f"Added {name} to contacts!")

    elif choice == "2":
        if len(contacts) ==0:
            print("No Contacts yet!")
        else:
            print("\n----All Contacts---")
            for name, details in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print()

    elif choice == "3":
        #Save contacts to file before exiting
        with open("contacts.txt","w") as file:
            for name, details in contacts.items():
                line = f"{name}|{details['phone']}|{details['email']}\n"
                file.write(line)
        print("Contacts saved!")
        print("Goodhye!")
        break
    else:
        print("Invalid choice")




