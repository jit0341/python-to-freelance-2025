# =========Configuration=============
inventories_file = "inventories.txt"
inventories = {}
SEPARATOR = "|"

#===========FILE OPERATION=========
def load_inventories():
    global inventories
    
    inventories = {}
    try:
        with open("inventories_file","r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(SEPARATOR)
                
                if len(parts) == 3:
                    product_name, price, quantity = parts
                    
                    inventories[product_name.title()] = {
                        "price": price,
                        "quantity": quantity
                    }
                    
        print("Inventories loaded successfully from inventories.txt.")
    except FileNotFoundError:
        print("No invetories file found! Starting fresh.")
    except Exception as e:
        print(f"An error occured during loading: {e}")
        
        inventories = {}
        
def save_inventories():
    try:
        with open("inventories_file","w") as file:
            for product_name,details in inventories.items():
                line = f"{product_name}{SEPARATOR}{details['price']}{SEPARATOR}{details['quantity']}\n"
                file.write(line)
        print("\nInventories saved successfully to inventories.txt.")
                
    except Exception as e:
        print(f"Error saving inventories: {e}")
        
# ============= CRUD Operations =============

def add_inventories():
    global inventories
    print("\n------Add new inventories------")
    
    product_name = input("Enter product name:").strip().title()
        
    if not product_name:
        print("Product name cannot be empty.")
        return
    if product_name in inventories:
        print(f"Inventory '{product_name}' already exists.")
        return
    price = input("Enter product price:").strip() or "N/A"
    quantity = input("Enter quantity").strip() or "N/A"
    
    inventories[product_name] = {
        "price": price,
        "quantity": quantity
    }
    print(f"Inventories '{product_name}' added successfully.")
    
def view_all_inventories():
    print("\n-----All inventories----")
    
    if not inventories:
        print("No inventories found. Add one.")
        return
    print(f"{'product_name': <20} {'price': <15} {'quantity': <30}")
    print("=" *65)
    
    
    for product_name, details in inventories.items():
        print(f"{product_name: <20} {details['price']: <15} {details['quantity']: <30}")
        
def search_inventory():