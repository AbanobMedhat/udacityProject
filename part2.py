import string

# Define function to evaluate password strength
def evaluate_password(password):
    # Define character sets
    uppercase_letters = set(string.ascii_uppercase)
    lowercase_letters = set(string.ascii_lowercase)
    numbers = set(string.digits)
    special_chars = set("!@#$%^&*()_+-=[]{};':\",./<>?")

    # Determine if password meets all criteria
    contains_uppercase = any(char in uppercase_letters for char in password)
    contains_lowercase = any(char in lowercase_letters for char in password)
    contains_number = any(char in numbers for char in password)
    contains_special = any(char in special_chars for char in password)
    is_valid_length = len(password) >= 8

    # Determine password strength category
    if contains_uppercase and contains_lowercase and contains_number and contains_special and is_valid_length:
        category = "Very Strong"
        description = "Your password meets all requirements and is considered very strong."
    elif (contains_uppercase and contains_lowercase and contains_number and is_valid_length) or (contains_uppercase and contains_lowercase and contains_special and is_valid_length) or (contains_lowercase and contains_number and contains_special and is_valid_length):
        category = "Strong"
        description = "Your password meets most requirements and is considered strong. To improve your password's strength, consider adding special characters or increasing its length."
    elif (contains_uppercase and contains_lowercase and is_valid_length) or (contains_lowercase and contains_number and is_valid_length) or (contains_uppercase and contains_number and is_valid_length):
        category = "Moderate"
        description = "Your password meets some requirements and is considered moderate. To improve your password's strength, consider adding numbers or special characters, or increasing its length."
    else:
        category = "Weak"
        description = "Your password does not meet the minimum requirements and is considered weak. To improve your password's strength, consider adding uppercase letters, lowercase letters, numbers, or special characters, or increasing its length."

    return category, description

# Prompt user to evaluate password
print("Welcome to the Password Security Strength Evaluator!")
password = input("Please enter your old password: ")
category, description = evaluate_password(password)
print("Your password falls under the category of:", category)
print("Description:", description)
