import mysql.connector

# Establish connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Default for XAMPP
        database="testdb"
    )
# UPDATE
def update_user(user_id, new_name, new_email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (new_name, new_email, user_id))
    conn.commit()
    print("User updated successfully.")
    conn.close()

# Call the function here
update_user(1, "David Johhanson", "david@example.com")
