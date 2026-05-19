import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="",    # change if needed
        database="bankdb"
    )

def login():
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT account_no, balance FROM accounts WHERE user_id=%s AND password=%s", (user_id, password))
    result = cursor.fetchone()
    db.close()

    if result:
        print("\n✅ Login Successful!\n")
        return result[0]
    else:
        print("\n❌ Invalid Login Credentials\n")
        return None

def check_balance(account_no):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (account_no,))
    balance = cursor.fetchone()[0]
    db.close()
    print(f"\n💰 Current Balance: ₹{balance}\n")

def deposit(account_no):
    amount = float(input("Enter amount to deposit: "))
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_no=%s", (amount, account_no))
    cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)", (account_no, "Deposit", amount))

    db.commit()
    db.close()
    print("\n✅ Amount Deposited Successfully!\n")

def withdraw(account_no):
    amount = float(input("Enter amount to withdraw: "))
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (account_no,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_no=%s", (amount, account_no))
        cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)", (account_no, "Withdraw", amount))
        db.commit()
        print("\n✅ Withdrawal Successful!\n")
    else:
        print("\n⚠️ Insufficient Balance!\n")

    db.close()

def transaction_history(account_no):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT type, amount, date FROM transactions WHERE account_no=%s", (account_no,))
    history = cursor.fetchall()
    db.close()

    print("\n📜 Transaction History:")
    for record in history:
        print(f"{record[0]} of ₹{record[1]} on {record[2]}")
    print()

def atm_menu(account_no):
    while True:
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Transaction History")
        print("5. Exit")
        choice = int(input("\nEnter choice: "))

        if choice == 1:
            check_balance(account_no)
        elif choice == 2:
            deposit(account_no)
        elif choice == 3:
            withdraw(account_no)
        elif choice == 4:
            transaction_history(account_no)
        elif choice == 5:
            print("\nThank You for Using ATM 😊")
            break
        else:
            print("\n❌ Invalid Choice\n")

# Main Program
account = login()
if account:
    atm_menu(account)
