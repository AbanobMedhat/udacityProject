import random
import string

# Define function to generate password
def generate_password():
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = "!@#$%^&*()_+-=[]{};':\",./<>?"

    # Combine character sets
    all_chars = uppercase_letters + lowercase_letters + numbers + special_chars

    # Generate password
    password = ""
    password += random.choice(uppercase_letters)
    password += random.choice(lowercase_letters)
    password += random.choice(numbers)
    password += random.choice(special_chars)
    password += ''.join(random.choice(all_chars) for i in range(4))
    password = ''.join(random.sample(password, len(password)))

    # Ensure password meets length requirement
    while len(password) < 12:
        password += random.choice(all_chars)

    return password

# Prompt user to generate password
print("Welcome to the Secure Password Generator!")
print("Your password will be 12 characters or longer, and contain at least one uppercase letter, one lowercase letter, one number, and may include special characters.")
print("Your password is:", generate_password())
