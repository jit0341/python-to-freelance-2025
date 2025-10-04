def add_expense(expenses):
    """Add a new expense to the list"""
    amount = float(input("Enter amount:"))
    category = input("Enter category:")
    description = input("Enter description:")
    expense = {"amount":amount, "category":category, "description":description}
    expenses.append(expense)
    print(f"Added ₹{amount} expense to {category}")

def view_all_expenses(expenses):
    """Display all expenses"""
    if len(expenses) == 0:
        print("No expenses recorded yet!")
    else:
        print("\n====All expenses====")
        for expense in expenses:
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print()
    pass

def view_total_by_category(expenses):
    """Show total for a specific category"""
    category = input("Enter category to view total:")
    total = 0
    for expense in expenses:
        if expense['category'] == category:
            total += expense['amount']
            if total == 0:

               print(f"No expenses found for category: {category}")
            else:
               print(f"Total spent on {category}: ₹{total}")
    pass

def save_and_exit(expenses):
    with open("expenses1.txt","w") as file:
        for expense in expenses:
            line = f"{expense['amount']}|{expense['category']}|{expense['description']}\n"
            file.write(line)
        print("Expense saved in a file")
        print("Goodbye!")

expenses = []

while True:
    print("\n===Menu===")
    print("1. Add expense")
    print("2. View all")
    print("3. View total by category")
    print("4. Exit")
    
    choice = input("Enter choice:")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_all_expenses(expenses)
    elif choice == "3":
        view_total_by_category(expenses)
    elif choice == "4":
        save_and_exit(expenses)
        break
    else:
        print("Invalid choice!")
