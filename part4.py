import hashlib

def generate_hash():
    # prompt the user for the file path
    file_path = input("Enter the path of the file to hash: ")

    # read the file
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # generate hash
    hash_value = hashlib.sha256(file_data).hexdigest()

    # write the hash to a file
    with open(file_path + '_hash.txt', 'w') as hash_file:
        hash_file.write(hash_value)

    print("Hash value generated and saved to '{}_hash.txt'.".format(file_path))

def check_integrity():
    # prompt the user for the data file path
    data_file_path = input("Enter the path of the data file to check: ")

    # prompt the user for the hash file path
    hash_file_path = input("Enter the path of the corresponding hash file: ")

    # read the data file
    with open(data_file_path, 'rb') as data_file:
        data = data_file.read()

    # generate hash
    hash_value = hashlib.sha256(data).hexdigest()

    # read the stored hash value from the hash file
    with open(hash_file_path, 'r') as hash_file:
        stored_hash_value = hash_file.read()

    # compare hash values and display message
    if hash_value == stored_hash_value:
        print("Integrity check passed. The data in the file '{}' is intact.".format(data_file_path))
    else:
        print("Integrity check failed. The data in the file '{}' has been modified.".format(data_file_path))

# prompt the user for the action to perform
action = input("Enter '1' to generate hash or '2' to check integrity: ")

if action == '1':
    generate_hash()
elif action == '2':
    check_integrity()
else:
    print("Invalid input. Please enter '1' or '2'.")
