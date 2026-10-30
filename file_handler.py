import os
import json
from product import Product

INVENTORY_FILE = "inventory.json"


def save_inventory(inventory):
    products_data = []
    for product in inventory.get_all_products():
        product_data = {
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }
        products_data.append(product_data)

    try:
        with open(INVENTORY_FILE, 'w') as file:
            json.dump(products_data, file, indent=4)

        return True

    except(OSError, json.JSONDecodeError) as e:
            return f"Error loading inventory: {e}"
    

# ======================================================================
# ======================================================================
# ======================================================================

def load_inventory(inventory):
    if not os.path.exists(INVENTORY_FILE):
        return "not_found"

    try:
        with open(INVENTORY_FILE, 'r') as file:
            products_data = json.load(file)

            for item in products_data:
                product = Product(
                    product_id=item["product_id"],
                    name=item["name"],
                    price=item["price"],
                    stock=item["stock"]
                )

                inventory.add_product(product)
            return "loaded"

    except(OSError, json.JSONDecodeError) as e:
        return "error"