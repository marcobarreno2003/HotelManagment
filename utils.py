# utils.py
import re

def validate_email(email):
    """
    Validates if the given email is in the correct format.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    if re.match(email_regex, email):
        return True
    print("Invalid email format.")
    return False

def validate_password(password):
    """
    Validates if the given password meets basic security requirements.
    
    Args:
        password (str): The password to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return False
    return True

def validate_hotel_name(hotel_name, graph):
    """
    Validates if a hotel name exists in the hotel graph.
    
    Args:
        hotel_name (str): The name of the hotel to check.
        graph (dict): The graph containing hotel locations.
    
    Returns:
        bool: True if the hotel exists in the graph, False otherwise.
    """
    if hotel_name in graph:
        return True
    print(f"Hotel '{hotel_name}' does not exist in the system.")
    return False

def validate_numeric_input(value):
    """
    Validates if the input is a numeric value (integer).
    
    Args:
        value (str): The value to check.
    
    Returns:
        bool: True if the value is a valid integer, False otherwise.
    """
    try:
        int(value)
        return True
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return False
