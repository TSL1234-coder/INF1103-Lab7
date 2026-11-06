from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def show_product_details(product: Product) -> None:
    # Works with any product, Doesn't check the subclass it receives
    product.display_information()
    print(product.get_fulfilment_info())


class BadDigitalProduct(DigitalProduct):

    def update_stock(self, quantity: int)-> None:
        raise NotImplementedError("Digital products have no stock")


supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
physical = PhysicalProduct("P001", "Laptop", 1200.00, 10, supplier, 2.5)
digital = DigitalProduct("D001", "E-book", 15.00, 100, supplier, 5.0)

print("=== 1. LSP: one function, both subclasses ===")
print("[PhysicalProduct]")
show_product_details(physical)
print("\n[DigitalProduct]")
show_product_details(digital)


print("\n=== 2. LSP: both subclasses keep Product's update_stock() contract ===")
products: list[Product] = [physical, digital]
for product in products:
    valid = product.update_stock(50)
    invalid = product.update_stock(-1)
    print(f"{product.get_name():<8} update_stock(50) -> {valid}, "
          f"update_stock(-1) -> {invalid}, stock = {product.get_stock()}")



print("\n=== 3. Polymorphism: one Inventory, one loop, no isinstance() ===")
inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

for product in inventory.get_all_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 20)

print("\n === 4. What LSP violation looks like ===")
bad = BadDigitalProduct("D002", "Broken E-book", 10.00, 5, supplier, 1.0)
mixed: list[Product] = [physical, digital, bad]
for product in mixed:
    try:
        product.update_stock(5)
        print(f"{type(product).__name__}: update_stock(5) worked")
    except NotImplementedError as error:
        print(f"{type(product).__name__}: CRASHED with NotImplementedError "
              f"({error})")