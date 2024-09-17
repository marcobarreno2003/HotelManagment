# db_connection.py
import mysql.connector

def connect_db():
    """
    Establishes a connection to the MySQL database.
    Returns:
        mysql.connector.connection.MySQLConnection: Connection object if successful, otherwise None.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Assuming you're using XAMPP
            user="root",       # Default MySQL user
            password="",       # Default password for MySQL (empty)
            database="hotel_reservas"  # The name of the database
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
