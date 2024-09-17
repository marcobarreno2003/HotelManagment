import mysql.connector

def connect_db():
    """
    Establishes a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Assuming you're using XAMPP or MySQL locally
            user="root",       # Default MySQL user
            password="",       # Default password for MySQL
            database="hotel_managment"  # Your database name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
