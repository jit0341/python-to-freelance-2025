#======CONFIGURATION===============
inventories_file = "inventories.txt"
inventories = {}
SEPARATOR = "|"

#========FILE OPERATIONS============
def load_inventories():
    global inventories
    inventories ={}
    try:
        with open(inventories_file,"r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(SEPARATOR)
                if len(parts) == 3:
                    product_name,price,quantity = parts
        print("Inventories loaded successfully from inventories.txt.")
    except FileNotFoundError:
        print(f"No inventories found. starting fresh!")
    except Exception as e:
        print(f"An error during loading: {e}")
        inventories = {}

def save_inventories():
    try:
        with open("inventories.txt","w") as file:
            for product_name,details in inventories.items():
                line = f"{product_name}{SEPARATOR}{details['price']}{SEPARATOR}{details['quantity']}\n"
                file.write(line)
        print(f"Inventories '{product_name}' saved successfully into inventories.txt")
    except Exception as e:
        print(f"Error saving inventories: {e}")
        inventories = {}

def add_inventories():
    global inventories
    print("------Add inventories-------")
    product_name = input("Enter product name:").strip().title()

    if not product_name:
        print("Product name cannot be empty.")
    if product_name in inventories:
        print(f"Product '{product_name}' already exists.")
        return
    

        price = input("Enter price:").strip() or "N/A"
        quantity = input("Enter quantity:").strip() or "N/A"

        inventories[product_name] = {
            "price": price,
            "quantity": quantity
        }
        print(f"Inventories '{product_name}' added successfully. ")
