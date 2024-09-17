import re

def validate_email(email):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    if re.match(email_regex, email):
        return True
    print("Invalid email format.")
    return False

def validate_password(password):
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return False
    return True

