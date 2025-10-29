#======Configuration===========
inventories_file = "inventories.txt"
inventories = {}
SEPARATOR = "|"

#=======File Operation=========
def load_inventories():
    global inventories
    inventories = {}
    try:
        with open(inventories_file,"r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(SEPARATOR)
                if len(parts) == 3:
                    product_name,price,quantity = parts
                    inventories[product_name.title()] = {
                    "price": price,
                    "quantity": quantity
                    }

        print("Inventories loaded successfully from inventories.txt")
        
    except FileNotFoundError:
        print("No inventories file found! starting fresh.")
    except Exception as e:
        print(f"Am error occurred durimg loading: {e}")
        inventories = {}
def save_inventories():
    try:
        with open("inventories.txt","w") as file:
            for product_name,details in inventories.items():
                line = f"{product_name}{SEPARATOR}{details['price']}{SEPARATOR}{details['quantity']}\n"
                file.write(line)
        print(f"\nInventories '{product_name}' saved successfully to inventories.txt")

    except Exception as e:
        print(f"Error saving inventories : {e}")

#============CRUD Operations===========
def add_inventory():
    global inventories
    print("\n----Adding Inventory-------")
    print("=" *65)

    product_name = input("Enter product:").strip().title()
    if not inventories:
        print("Product name cannot be empty")
        return
    if product_name in inventories:
        print(f"Inventory'{product_name}' already exists.")
        return
    price = input("Enter price:").strip() or "N/A"
    quantity = input("Enter quantity:").strip() or "N/A"

    inventories[product_name.title()] = {
            "price": price,
            "quantity": quantity
            }
    print(f"Inventories '{product_name}' added successfully.")

def view_all_inventories():
    print("\n------View Inventories-------")

    if not inventories:
        print("No inventories found! Add one.")
        return
    print(f" {'product_name': <20}{'price': <15}{'quantity': <30}")
    print("=" *65)

    for product_name,details in inventories.items():
        print(f" {product_name:<20} {details['price']:<15} {details['quantity']:<30}")

def search_inventory():
    print("\n-----Searching Inventory-----")

    search_term = input("Enter product name to search:").strip().title()
    if search_term in inventories:
        details = inventories[search_term]
        print(f"\nFound inventory: {search_term}")
        print(f" {details['price']} ")
        print(f" {details['quantity']} ")

    else:
        print(f" Inventory'{search_term}' not found")

def delete_inventory():
    global inventories
    print("\n------Deleting Inventory------")
    product_name_to_delete = input("Enter product name to delete:")
    if product_name_to_delete in inventories:
        confirm = input(f" Are you sure want to delete '{product_name_to_delete}'? (y/n):").lower()
        if confirm == 'y':
            del inventories[product_name_to_delete]
            print(f"Inventory'{product_name_to_delete}' deleted successfully")
        else:
            print(f" Inventories'{product_name_to_delete}' not found!")

#====================================
#        Main Menu
#====================================

def main_menu():
    load_inventories()

    while True:
        print("\n" + "=" *30)
        print("Inventory Management System")
        print("-" *30)
        print("1. Add Inventory")
        print("2. View All Inventories")
        print("3. Search Inventory")
        print("4. Delete Inventory")
        print("5. Exit and save")
        print("-" *30)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_inventory()
        elif choice == "2":
            view_all_inventories()
        elif choice == "3":
            search_inventory()
        elif choice == "4":
            delete_inventory()
        elif choice == "5":
            save_inventories()
            print("Thank you for using inventory management system. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter choice 1 to 5.")

#=======Run the program =======
if __name__ == "__main__":
    main_menu()







