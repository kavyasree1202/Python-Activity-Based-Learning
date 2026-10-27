
# Food Supply Chain Stock Reconciliation

locations = int(input("Enter number of locations: "))

minimum_stock = int(input("Enter minimum required stock: "))

total_received = 0
total_distributed = 0
total_damaged = 0
total_remaining = 0
total_discrepancy = 0
total_replenishment = 0

for i in range(locations):
    print("\n--- Location", i + 1, "---")

    name = input("Enter location name: ")
    opening = int(input("Enter opening stock: "))
    received = int(input("Enter quantity received: "))
    distributed = int(input("Enter quantity distributed: "))
    damaged = int(input("Enter quantity damaged: "))
    actual = int(input("Enter actual remaining stock: "))

    expected = opening + received - distributed - damaged
    discrepancy = actual - expected

    replenishment = max(0, minimum_stock - actual)

    print("\nLocation:", name)
    print("Expected remaining stock:", expected)
    print("Actual remaining stock:", actual)

    if discrepancy == 0:
        print("Stock Status: No discrepancy")
    else:
        print("Stock Discrepancy:", discrepancy)

    print("Replenishment Required:", replenishment)

    total_received += received
    total_distributed += distributed
    total_damaged += damaged
    total_remaining += actual
    total_discrepancy += discrepancy
    total_replenishment += replenishment

print("\n===== FINAL STOCK SUMMARY =====")
print("Total Locations:", locations)
print("Total Received:", total_received)
print("Total Distributed:", total_distributed)
print("Total Damaged:", total_damaged)
print("Total Actual Remaining:", total_remaining)
print("Net Stock Discrepancy:", total_discrepancy)
print("Total Replenishment Required:", total_replenishment)