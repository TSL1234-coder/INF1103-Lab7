# ======================================================================
# =================
# Import class
# =================
# ======================================================================


from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from file_handler import save_inventory, load_inventory, INVENTORY_FILE


# ======================================================================
# =================
# Functions
# =================
# ======================================================================

def create_default_products():
    return [
        PhysicalProduct("1001", "Keyboard", 30.00, 10, 0.8),
        PhysicalProduct("1002", "Mouse", 20.00, 15, 0.1),
        PhysicalProduct("1003", "Monitor", 150.00, 5, 4.5),
        PhysicalProduct("1004", "Printer", 200.00, 3, 7.0),
        DigitalProduct("1005", "Photo Editor", 59.90, 100, 250.0),
        DigitalProduct("1006", "E-book", 15.00, 100, 5.0),
    ]

def show_menu():
    print("\n--------Inventory Management System--------")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Product Stock")
    print("4. Search for Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-------------------------------------------")


def add_product_input(inventory):
    print("\nProduct type:")
    print("1. Physical Product")
    print("2. Digital Product")
    type_choice = input("Enter product type (1 or 2): ")

    if type_choice not in ('1', '2'):
        print("Invalid choice. Please enter 1 or 2.")
        return


    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Product Stock: "))

    if type_choice == '1':
        weight = float(input("Enter Product Weight (in kg): "))
        new_product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = float(input("Enter Product Download Size (in MB): "))
        new_product = DigitalProduct(product_id, name, price, stock, download_size)

    if inventory.add_product(new_product):
        print(f"Product {name} added successfully!")
    

def update_product_stock_input(inventory):
    product_id = input("Enter Product ID to update stock: ")

    product = inventory.search_product(product_id)
    if product is None:
        print(f"Product with ID {product_id} not found.")
        return

    new_stock = int(input(f"Enter new stock for {product.get_name()}: "))
    if product.update_stock(new_stock):
        print(f"Stock for {product.get_name()} updated to {new_stock}.")
    else:
        print(f"Failed to update stock for {product.get_name()}. Please check the input value.")


def search_product_input(inventory):
    product_id = input("Enter Product ID to search: ")

    product = inventory.search_product(product_id)
    if product is None:
        print(f"\nProduct with ID {product_id} not found.")
    else:
        print("\nProduct found:")
        product.display_information()



def save_inventory_ui(inventory):
    result = save_inventory(inventory)

    if result:
        print("\nInventory saved successfully!")
    else:
        print("\nError saving inventory!")



def setup_inventory(inventory):
    result = load_inventory(inventory)

    if result == "loaded":
        print("\nInventory loaded successfully!")
    elif result == "not_found":
        print(f"\nInventory file '{INVENTORY_FILE}' not found. Starting with an empty inventory.")

        for product in create_default_products():
            inventory.add_product(product)
        save_inventory(inventory)
        print("\nA new inventory file has been created with default products.")
    else:
        print("\nError loading inventory!")



# ======================================================================
# =================
# Main program
# =================
# ======================================================================

def main():
    print("=================================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=================================================================")

    # Create an instance of Inventory
    inventory = Inventory() 

    # Load inventory from file if it exists
    setup_inventory(inventory)  

   


    exit_program = False
    while not exit_program:
        show_menu()
        choice = input("Enter your choice (1-6): ")


        if choice == '1':
            inventory.display_all()
        elif choice == '2':
            add_product_input(inventory)
        elif choice == '3':
            update_product_stock_input(inventory)
        elif choice == '4':
            search_product_input(inventory)
        elif choice == '5':
            save_inventory_ui(inventory)
        elif choice == '6':
            save_inventory_ui(inventory)
            print("\nThank you for using the Inventory Management System. Goodbye!")
            exit_program = True
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()