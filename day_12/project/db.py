import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",        # change if needed
    password=""     # change if needed
)

cursor = db.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS bankdb")
cursor.execute("USE bankdb")

# Create accounts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_no INT PRIMARY KEY,
    user_id VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    balance DOUBLE
)
""")

# Create transaction history table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_no INT,
    type VARCHAR(20),
    amount DOUBLE,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert sample data
cursor.execute("INSERT IGNORE INTO accounts VALUES (1001, 'user1', 'pass1', 12000)")
cursor.execute("INSERT IGNORE INTO accounts VALUES (1002, 'user2', 'pass2', 15000)")
cursor.execute("INSERT IGNORE INTO accounts VALUES (1003, 'user3', 'pass3', 18000)")

db.commit()
db.close()
print("✅ Database and sample data created successfully!")
