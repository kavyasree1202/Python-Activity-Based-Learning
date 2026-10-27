
# Multi-Product Shopping Budget Constraint

budget = float(input("Enter your total budget: ₹"))
n = int(input("Enter number of products: "))

products = []

for i in range(n):
    print(f"\nProduct {i + 1}")
    name = input("Enter product name: ")
    price = float(input("Enter price per item: ₹"))
    quantity = int(input("Enter quantity: "))

    subtotal = price * quantity

    # Apply 10% discount when subtotal is ₹1000 or more
    if subtotal >= 1000:
        discount = subtotal * 0.10
    else:
        discount = 0

    total = subtotal - discount

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "discount": discount,
        "total": total
    })

# Calculate total shopping cost
total_cost = sum(p["total"] for p in products)

print("\n----- SHOPPING BILL -----")

for p in products:
    print(f"\nProduct: {p['name']}")
    print(f"Price: ₹{p['price']:.2f}")
    print(f"Quantity: {p['quantity']}")
    print(f"Discount: ₹{p['discount']:.2f}")
    print(f"Final cost: ₹{p['total']:.2f}")

print(f"\nTotal cost: ₹{total_cost:.2f}")
print(f"Budget: ₹{budget:.2f}")

# Reduce purchases if budget is exceeded
if total_cost > budget:
    excess = total_cost - budget
    print(f"\nBudget exceeded by ₹{excess:.2f}")
    print("Reduce the following purchases:")

    for p in sorted(products,
                    key=lambda x: x["price"],
                    reverse=True):
        while p["quantity"] > 0 and total_cost > budget:
            old_total = p["total"]
            p["quantity"] -= 1

            subtotal = p["price"] * p["quantity"]

            if subtotal >= 1000:
                discount = subtotal * 0.10
            else:
                discount = 0

            p["discount"] = discount
            p["total"] = subtotal - discount
            total_cost += p["total"] - old_total

            if p["quantity"] >= 0:
                print(
                    f"{p['name']}: quantity reduced "
                    f"to {p['quantity']}"
                )

    print(f"\nAdjusted total: ₹{total_cost:.2f}")

    if total_cost > budget:
        print("Budget cannot be met with available products.")
    else:
        print("Shopping is now within budget!")

else:
    print("\nShopping is within budget!")
