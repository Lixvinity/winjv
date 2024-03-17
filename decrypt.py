from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

directories = {
    "Desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "Downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "Documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "Music": os.path.join(os.path.expanduser("~"), "Music"),
    "Videos": os.path.join(os.path.expanduser("~"), "Videos"),
    "Pictures": os.path.join(os.path.expanduser("~"), "Pictures")
    }


# Original decryption function
def decrypt_file(encrypted_file_path, key):
    # Check if key length is 24 characters
    if len(key) != 24:
        raise ValueError("Key length must be 24 characters")

    # Read salt, IV, and ciphertext from the encrypted file
    with open(encrypted_file_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        ciphertext = f.read()

    # Derive the key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    derived_key = kdf.derive(key.encode())

    # Create cipher object using AES in CBC mode with PKCS7 padding
    cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Overwrite the encrypted file with decrypted data
    with open(encrypted_file_path, 'wb') as f:
        f.write(unpadded_data)

    print("Decryption successful. Encrypted file overwritten.")

# Function to decrypt all files in subfolders of a parent folder
def decrypt_files_in_folder(parent_folder, key):
    # Iterate over all items in the parent folder
    for filename in os.listdir(parent_folder):
        filepath = os.path.join(parent_folder, filename)
        # Check if the item is a directory
        if os.path.isdir(filepath):
            # Recursively decrypt files in subdirectories
            decrypt_files_in_folder(filepath, key)
        else:
            # Decrypt file if it's not a directory
            try:
                print(f"Decrypting file: {filepath}")
                decrypt_file(filepath, key)
                print("Decryption successful.")
            except Exception as e:
                print(f"Failed to decrypt {filename}: {e}")

# Function to start the decryption process
def start():
    print("Warning: Any errors in your key will result in your files being unrecoverable.")
    key = input("Enter the decryption key: ")
    for folder_name, folder_path in directories.items():
        decrypt_files_in_folder(folder_path, key)

# Entry point of the script
if __name__ == "__main__":
    start()
