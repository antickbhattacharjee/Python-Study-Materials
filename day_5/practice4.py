balance = 15000
while True:
    print("\nBanking System Menu:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ₹{amount}. Current balance: ₹{balance}")
        else:
            print("Invalid deposit amount.")
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrew ₹{amount}. Current balance: ₹{balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient balance.")
    elif choice == "3":
        print(f"Current balance: ₹{balance}")
    elif choice == "4":
        print("Exiting the banking system.")
        break
    else:
        print("Invalid choice. Please try again.")