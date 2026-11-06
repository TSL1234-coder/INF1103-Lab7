from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")

# Product created independently
guitar = PhysicalProduct("P002", "Guitar", 450.00, 5, supplier, 3.5)
print("--- 1. Product created on its own ---")
guitar.display_information()

inventory_a = Inventory()
inventory_b = Inventory()

# Add to Inventory A
inventory_a.add_product(guitar)
print("\n --- 2. Added to Inventory A ---")
print(f"Inventory A holds this exact object? "
      f"{inventory_a.find_product('P002') is guitar}")


# Remove from Inventory A
inventory_a.remove_product("P002")
print("\n--- 3. Removed from Inventory A ---")
print(f"Inventory A is empty? {inventory_a.is_empty()}")
print(f"find_product('P002):  {inventory_a.find_product('P002')}")
print("The Product still exists and stills works")
guitar.update_stock(7)
guitar.display_information()

# Add SAME object to Inventory B
inventory_a.add_product(guitar)
print("\n--- 4. Same Product object added to Inventory B ---")
print(f"Inventory B holds the same object? "
      f"{inventory_b.find_product('P002') is guitar}")

print(f"Stock carried over to B (7)? {guitar.get_stock()}")

print("\nRemoving a Product from an Inventory removes only the reference, "
      "so the Product is not destroyed.")

