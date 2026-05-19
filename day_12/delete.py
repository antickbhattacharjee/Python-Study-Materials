import mysql.connector

# Establish connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Default for XAMPP
        database="testdb"
    )
# DELETE
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    print("User deleted successfully.")
    conn.close()

# Call the function here
delete_user(1)  # Replace with the actual user ID to delete