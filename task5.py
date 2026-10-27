# ATM Transaction Sequence Simulation

balance = 5000
withdrawal_limit = 10000
transactions = []

print("===== ATM TRANSACTION SYSTEM =====")
print("Initial Balance: Rs.", balance)

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = input("Enter your choice (1 or 2): ")
    amount = float(input("Enter amount: Rs. "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        transactions.append("Invalid transaction")

    elif choice == "1":
        balance += amount
        print("Deposit successful.")
        transactions.append(f"Deposit: Rs. {amount:.2f}")

    elif choice == "2":
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded!")
            transactions.append("Withdrawal limit exceeded")

        elif amount > balance:
            print("Insufficient balance!")
            transactions.append("Insufficient balance")

        else:
            balance -= amount
            print("Withdrawal successful.")
            transactions.append(f"Withdrawal: Rs. {amount:.2f}")

    else:
        print("Invalid choice!")
        transactions.append("Invalid choice")

print("\n===== TRANSACTION SUMMARY =====")

for transaction in transactions:
    print(transaction)

print("Final Balance: Rs.", round(balance, 2))
print("Total Transactions:", len(transactions))
print("Thank you for using the ATM!")
