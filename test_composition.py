from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, supplier, 2.5)
ebook = DigitalProduct("D001", "E-book", 15.00, 100, supplier, 5.0)


def show_order(order: Order) -> None:
    print(f"Order {order.get_order_id()}")
    for product, quantity, subtotal in order.get_order_lines():
        print(f" {product.get_name(): <10} x {quantity} = ${subtotal:.2f}")

    print(f" Total: ${order.calculate_total():.2f}")



# 1. The Order creates its own OrderLines (we only pass Product + quantity).
order1 = Order("O001")
order1.add_order_line(laptop, 1)
order1.add_order_line(ebook, 3)
print("--- 1. Order O001 ---")
show_order(order1)

# 2. The SAME Product goes into a different Order.
order2 = Order("O002")
order2.add_order_line(laptop, 2)
print("\n--- 2. Order O002 uses the same laptop ---")
show_order(order2)

# 3. Count the objects. (Peeking at private attributes is for this test only.)
line_in_order1 = order1._Order__order_lines[0]  # type: ignore[attr-defined]
line_in_order2 = order2._Order__order_lines[0]  # type: ignore[attr-defined]
print("\n--- 3. Product objects vs OrderLine objects ---")
print(f"Same Product in both orders?   "
      f"{line_in_order1.get_product() is line_in_order2.get_product()}")
print(f"Same OrderLine in both orders? {line_in_order1 is line_in_order2}")
print("Product objects for the laptop: 1 (shared)")
print("OrderLine objects for the laptop: 2 (one per order)")

# 4. Removing a line goes through the Order. The Product survives.
print("\n--- 4. Remove the e-book line from O001 via the Order ---")
order1.remove_order_line(1)
show_order(order1)
print(f"The e-book Product still exists: {ebook.get_name()}")
print("\nOrderLine objects are only reachable through their Order, so a line "
      "cannot be moved to another Order.")
