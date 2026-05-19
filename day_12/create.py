# create.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testdb"
    )

def create_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("User created successfully.")
    conn.close()

# Call the function here
create_user("John Doe", "john@example.com")
