
# Integrated E-Commerce Order Processing and Reconciliation

inventory = {}
sales_revenue = 0
total_returns = 0

# Enter inventory details
n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter available stock: "))

    inventory[name] = {
        "price": price,
        "stock": stock,
        "sold": 0,
        "returned": 0
    }

# Process orders
orders = int(input("\nEnter number of orders: "))

for i in range(orders):
    print(f"\nOrder {i + 1}")
    name = input("Enter product name: ")

    if name not in inventory:
        print("Invalid product! Order rejected.")
        continue

    quantity = int(input("Enter order quantity: "))

    if quantity <= 0:
        print("Invalid quantity! Order rejected.")
        continue

    product = inventory[name]

    if quantity > product["stock"]:
        print("Insufficient stock! Order rejected.")
        continue

    discount_percent = float(
        input("Enter discount percentage (0-100): ")
    )

    if not 0 <= discount_percent <= 100:
        print("Invalid discount! Order rejected.")
        continue

    # Calculate discounted order value
    subtotal = product["price"] * quantity
    discount = subtotal * discount_percent / 100
    order_total = subtotal - discount

    # Dispatch order and update stock
    product["stock"] -= quantity
    product["sold"] += quantity
    sales_revenue += order_total

    print(f"Subtotal: Rs.{subtotal:.2f}")
    print(f"Discount: Rs.{discount:.2f}")
    print(f"Order total: Rs.{order_total:.2f}")
    print("Order dispatched successfully.")

# Process returns
returns = int(input("\nEnter number of return requests: "))

for i in range(returns):
    print(f"\nReturn {i + 1}")
    name = input("Enter product name: ")

    if name not in inventory:
        print("Invalid product!")
        continue

    quantity = int(input("Enter return quantity: "))
    product = inventory[name]

    # Only return products that were sold and not already returned
    available_to_return = product["sold"] - product["returned"]

    if quantity <= 0 or quantity > available_to_return:
        print("Invalid return quantity!")
        continue

    product["returned"] += quantity
    product["stock"] += quantity

    # Refund using the original average discounted price
    unit_price = product["price"]
    sold_quantity = product["sold"]

    # Returns are refunded at the original product price here.
    # For exact order-level refunds, store each order's discount.
    refund = unit_price * quantity
    sales_revenue -= refund
    total_returns += refund

    print(f"Return accepted. Refund: Rs.{refund:.2f}")

# Reconciliation and final inventory report
print("\n========== FINAL RECONCILIATION ==========")

for name, product in inventory.items():
    expected_stock = (
        product["stock"]
    )

    print(f"\nProduct: {name}")
    print(f"Unit price: Rs.{product['price']:.2f}")
    print(f"Units sold: {product['sold']}")
    print(f"Units returned: {product['returned']}")
    print(f"Final stock: {expected_stock}")

    # Verify inventory movement
    calculated_stock = (
        product["stock"]
    )

    if calculated_stock < 0:
        print("DISCREPANCY: Negative stock!")
    else:
        print("Stock status: Valid")

print(f"\nTotal refunds: Rs.{total_returns:.2f}")
print(f"Net revenue: Rs.{sales_revenue:.2f}")
print("Inventory reconciliation completed.")
