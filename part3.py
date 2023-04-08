import string
import random
import hashlib

# Define function to encrypt data
def encrypt_data(data, key):
    # Rule 1: Caesar cipher
    caesar_shift = random.randint(1, 25)
    caesar_cipher = "".join([chr((ord(char) - 97 + caesar_shift) % 26 + 97) if char.isalpha() else char for char in data])
    
    # Rule 2: Substitution cipher
    substitution_key = "".join(random.sample(string.ascii_letters, len(string.ascii_letters)))
    substitution_cipher = "".join([substitution_key[ord(char) - 97] if char.isalpha() else char for char in data.lower()])
    
    # Rule 3: Hashing
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    hashed_key = hashlib.sha256(key.encode()).hexdigest()
    hash_cipher = "".join([chr((ord(data[i]) + ord(hashed_key[i % len(hashed_key)]) - 2 * ord('a')) % 26 + ord('a')) if data[i].isalpha() else data[i] for i in range(len(data))])

    return caesar_cipher, substitution_cipher, hash_cipher

# Define function to decrypt data
def decrypt_data(data, key):
    # Rule 1: Caesar cipher
    caesar_shift = 25 - int(key[0])
    caesar_cipher = "".join([chr((ord(char) - 97 + caesar_shift) % 26 + 97) if char.isalpha() else char for char in data])

    # Rule 2: Substitution cipher
    substitution_key = key[1:]
    substitution_plain = "".join([string.ascii_lowercase[substitution_key.index(char)] if char.isalpha() else char for char in data])
    
    # Rule 3: Hashing
    hashed_data = hashlib.sha256(substitution_plain.encode()).hexdigest()
    hashed_key = hashlib.sha256(key.encode()).hexdigest()
    hash_plain = "".join([chr((ord(data[i]) - ord(hashed_key[i % len(hashed_key)]) + ord('a')) % 26 + ord('a')) if data[i].isalpha() else data[i] for i in range(len(data))])

    return caesar_cipher, substitution_plain, hash_plain

# Prompt user for input
print("Welcome to the Data Confidentiality Application!")
mode = input("Enter 'e' for encryption or 'd' for decryption: ")
if mode == 'e':
    input_file = input("Enter the path of the file to be encrypted: ")
    output_file = input("Enter the path of the output file: ")
    encryption_key = input("Enter a key for encryption: ")
    with open(input_file, 'r') as file:
        plaintext = file.read()
    caesar_cipher, substitution_cipher, hash_cipher = encrypt_data(plaintext, encryption_key)
    with open(output_file, 'w+') as file:
        file.write("Caesar cipher:\n" + caesar_cipher + "\n\nSubstitution cipher:\n" + substitution_cipher + "\n\nHashing:\n" + hash_cipher)
    print("Encryption complete! Output written to", output_file)
elif mode == 'd':
    input_file = input("Enter the path of the file to be decrypted: ")
    output_file = input("Enter the path of the output file: ")
    decryption_key = input("Enter the key for decryption: ")
    with open(input_file, 'r') as file:
        ciphertext = file.read()
    caesar_cipher, substitution_cipher,
