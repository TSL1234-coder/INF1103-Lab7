from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# Supplier created independently, before any Product exists
supplier = Supplier("S001", "Tech Supplies Inc.", "sales@techsupplies.com")
print("--- Supplier on its own (no products yet) ---")
supplier.display_information()


# Two products receive from SAME supplier
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, supplier, 2.5)
ebook = DigitalProduct("D001", "E-book", 15.00, 100, supplier, 5)

print("\n--- Supplier Information after products are created ---")
print("Via physical product:")
laptop.get_supplier().display_information()
print("\nVia digital product:")
ebook.get_supplier().display_information() 


print("\n--- Separate Objects, one shared Supplier ---")
print(f"laptop is ebook?   {laptop is ebook}")
print(f"laptop is supplier? {laptop is supplier}")
print(f"Both products share the same supplier? {laptop.get_supplier() is ebook.get_supplier()}")


print("\n--- After 'del supplier' ---")
del supplier
print("Supplier object deleted.")
print("Laptop's supplier information:", laptop.get_supplier().get_name())
print("E-book's supplier information:", ebook.get_supplier().get_name())
print("\nThe products still have access to the supplier information, demonstrating that the association is maintained even after the original supplier reference is deleted.")
