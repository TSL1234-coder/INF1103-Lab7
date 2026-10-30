from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

physical = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5)
digital = DigitalProduct("D001", "E-book", 15.00, 100, 5)

print("---Physical Product Information---")
physical.display_information()
print(f"Fulfillment Info: {physical.get_fulfillment_info()}")

print("\n---Digital Product Information---")
digital.display_information()
print(f"Fulfillment Info: {digital.get_fulfillment_info()}")


print("\n--- Abstract Class Test ---")
try:
    product = Product("A001", "Abstract Product", 0.00, 0)
except TypeError as e:
    print(f"Error: {e}")