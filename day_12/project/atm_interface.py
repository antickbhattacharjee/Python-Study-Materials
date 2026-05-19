import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector

# ---------------- Database Connection ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="",        # change if needed
        database="bankdb"
    )

# ---------------- Core Functionalities ----------------
def login_action():
    user_id = user_id_entry.get()
    password = password_entry.get()

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT account_no FROM accounts WHERE user_id=%s AND password=%s", (user_id, password))
    result = cursor.fetchone()
    db.close()

    if result:
        global current_account
        current_account = result[0]
        messagebox.showinfo("Login Successful", "Welcome to your account!")
        login_window.destroy()
        open_atm_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid User ID or Password")

def check_balance():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (current_account,))
    balance = cursor.fetchone()[0]
    db.close()
    messagebox.showinfo("Current Balance", f"Your current balance is ₹{balance}")

def deposit_amount():
    amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
    if amount and amount > 0:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_no=%s", (amount, current_account))
        cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)",
                       (current_account, "Deposit", amount))
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Amount deposited successfully!")
    else:
        messagebox.showwarning("Invalid", "Please enter a valid amount.")

def withdraw_amount():
    amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
    if amount and amount > 0:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (current_account,))
        balance = cursor.fetchone()[0]

        if balance >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_no=%s", (amount, current_account))
            cursor.execute("INSERT INTO transactions (account_no, type, amount) VALUES (%s, %s, %s)",
                           (current_account, "Withdraw", amount))
            db.commit()
            messagebox.showinfo("Success", "Withdrawal successful!")
        else:
            messagebox.showerror("Error", "Insufficient balance!")
        db.close()
    else:
        messagebox.showwarning("Invalid", "Please enter a valid amount.")

def view_transactions():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT type, amount, date FROM transactions WHERE account_no=%s", (current_account,))
    records = cursor.fetchall()
    db.close()

    history_text = "\n".join([f"{r[0]} ₹{r[1]} on {r[2]}" for r in records])
    if not history_text:
        history_text = "No transactions yet."
    messagebox.showinfo("Transaction History", history_text)

def logout():
    messagebox.showinfo("Logout", "Thank you for using the ATM!")
    atm_window.destroy()

# ---------------- GUI Windows ----------------
def open_atm_menu():
    global atm_window
    atm_window = tk.Tk()
    atm_window.title("💳 ATM Menu")
    atm_window.geometry("400x400")
    atm_window.config(bg="#e8f0fe")

    tk.Label(atm_window, text="ATM Main Menu", font=("Arial", 16, "bold"), bg="#e8f0fe").pack(pady=20)

    tk.Button(atm_window, text="Check Balance", width=20, command=check_balance).pack(pady=10)
    tk.Button(atm_window, text="Deposit Amount", width=20, command=deposit_amount).pack(pady=10)
    tk.Button(atm_window, text="Withdraw Amount", width=20, command=withdraw_amount).pack(pady=10)
    tk.Button(atm_window, text="Transaction History", width=20, command=view_transactions).pack(pady=10)
    tk.Button(atm_window, text="Exit", width=20, command=logout, bg="#ff4d4d", fg="white").pack(pady=20)

    atm_window.mainloop()

# ---------------- Login Window ----------------
login_window = tk.Tk()
login_window.title("🏦 ATM Login")
login_window.geometry("400x300")
login_window.config(bg="#e8f0fe")

tk.Label(login_window, text="ATM Login System", font=("Arial", 16, "bold"), bg="#e8f0fe").pack(pady=20)

tk.Label(login_window, text="User ID:", bg="#e8f0fe").pack()
user_id_entry = tk.Entry(login_window, width=30)
user_id_entry.pack(pady=5)

tk.Label(login_window, text="Password:", bg="#e8f0fe").pack()
password_entry = tk.Entry(login_window, width=30, show="*")
password_entry.pack(pady=5)

tk.Button(login_window, text="Login", width=15, command=login_action, bg="#4caf50", fg="white").pack(pady=20)

login_window.mainloop()
