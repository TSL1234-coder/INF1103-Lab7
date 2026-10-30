from physical_product import PhysicalProduct
from digital_product import DigitalProduct

physical = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5)
digital = DigitalProduct("D001", "E-book", 15.00, 100, 5)

print("---Physical Product Information---")
physical.display_information()

print("\n---Digital Product Information---")
digital.display_information()