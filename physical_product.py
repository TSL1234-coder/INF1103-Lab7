from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_COST = 5.00  # Base shipping cost in dollars
    RATE_PER_KG = 2.00  # Rate per kilogram in dollars

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self.BASE_SHIPPING_COST + (self.RATE_PER_KG * self.__weight)