import os
import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

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

        if isinstance(product, PhysicalProduct):
            product_data["type"] = "physical"
            product_data["weight"] = product.get_weight()
        elif isinstance(product, DigitalProduct):
            product_data["type"] = "digital"
            product_data["download_size"] = product.get_download_size()

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

                product_type = item["type"]

                if product_type == "physical":
                    product = PhysicalProduct(
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        stock=item["stock"],
                        weight=item["weight"]
                    )
                elif product_type == "digital":
                    product = DigitalProduct(
                        product_id=item["product_id"],
                        name=item["name"],
                        price=item["price"],
                        stock=item["stock"],
                        download_size=item["download_size"]
                    )
                else:
                    print(f"Unknown product type: {product_type}. Skipping this product.")
                    continue

                inventory.add_product(product)
            return "loaded"

    except(OSError, json.JSONDecodeError) as e:
        return "error"