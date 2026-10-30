class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print(f"Product with ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return

        print("\nCurrent Inventory:\n")
        for product in self.__products:
            product.display_product_info()
            print("-" * 20)


    def get_all_products(self):
        return list(self.__products)

    def is_empty(self):
        return len(self.__products) == 0