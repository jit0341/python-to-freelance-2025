expenses = []

while True:
    print("\n===Menu===")
    print("\n1. Add expense")
    print("2. View all ")
    print("3. View total by category")
    print("4. Exit")
    
    choice = input("Enter choice:")

    if choice == "1":
        amount = float(input("Enter amount:"))
        category = input("Enter category(Food/Rent/Transport/etc):")
        description = input("Enter description:")
        expense = {"amount":amount,"category":category,"description":description}
        expenses.append(expense)
        print(f"Added ₹{amount} expense to {category}")


    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet!")
        else:
            print("\n====All expenses====")
            for expense in expenses:
                print(f"Amount: ₹{expense['amount']}")
                print(f"Category: {expense['category']}")
                print(f"Description: {expense['description']}")
                print()


    elif choice == "3":
        category = input("Enter category to view total:")
        total = 0
        for expense in expenses:
            if expense['category'] == category:
                total += expense['amount']
        if total == 0:
            print(f"No expenses found for category: {category}")
        else:
            print(f"Total spent on {category}: ₹{total}")
    elif choice == "4":
        with open("expenses.txt","w") as file:
            for expense in expenses:
                line = f"{expense['amount']}|{expense['category']}|{expense['description']}"
                file.write(line)
                print("Expense saved in a file")
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")


        
        








