from product import Product

class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if self.find_product(product.get_product_id()) is not None:
            print(f"Product with ID {product.get_product_id()} already exists.")
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id: 
                return product
        return None

    def display_all(self) -> None:
        if not self.__products:
            print("No products in inventory.")
            return

        print("\nCurrent Inventory:\n")
        for product in self.__products:
            product.display_information()
            print("-" * 20)


    def get_all_products(self) -> list[Product]:
        return list(self.__products)

    def is_empty(self) -> bool:
        return len(self.__products) == 0