from product import Product
from can_be_shipped import CanBeShipped
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

physical = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5)
digital = DigitalProduct("D001", "E-book", 15.00, 100, 5)

print("---Physical Product Information---")
physical.display_information()
print(f"Fulfillment Info: {physical.get_fulfilment_info()}")

print("\n---Digital Product Information---")
digital.display_information()
print(f"Fulfillment Info: {digital.get_fulfilment_info()}")


print("\n--- Abstract Class Test ---")
try:
    product = Product("A001", "Abstract Product", 0.00, 0)
except TypeError as e:
    print(f"Error: {e}")


print("\n--- CanBeShipped Interface Test ---")
try:
    shippable = CanBeShipped()
    print("ERROR: CanBeShipped instance created successfully, which should not happen. It shoudl be abstract!")
except TypeError as e:
    print(f"Error: {e}")


print("\n--- Shipping Cost Calculation ---")
light = PhysicalProduct("P002", "Lightweight Item", 50.00, 20, 0.5)
medium = PhysicalProduct("P003", "Mediumweight Item", 100.00, 15, 3)
heavy = PhysicalProduct("P003", "Heavy Item", 200.00, 5, 10)

for item in [light, medium, heavy]:
    print(f"{item.get_name()} (Weight: {item.get_weight()} kg) - Shipping Cost: ${item.calculate_shipping_cost():.2f}")

print("\n--- Digital product does not need shipping ---")
print(f"DigitalProduct is a CanBeShipped? {isinstance(digital, CanBeShipped)}")
print(f"PhysicalProduct is a CanBeShipped? {isinstance(physical, CanBeShipped)}")