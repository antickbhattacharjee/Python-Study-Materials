import mysql.connector

# Establish connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Default for XAMPP
        database="testdb"
    )
# READ
def read_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    conn.close()

# Call the function here
read_users()