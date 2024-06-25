import os
import requests
from tqdm import tqdm
import random
import datetime
from colorama import init,Fore
class InsFSAZOM:
    def __init__(self):
        self.main()

    def main(self):
        print(f"{Fore.RED}Downloading files from GitHub The link must start with (https://raw.githubusercontent.com/User-Name/Your-Repository/main)")
        GITHUB_URL = input(f"{Fore.BLUE}Enter the GitHub URL to download files: ")
        print(f"{Fore.RED}")
        files_input = input(f"{Fore.YELLOW}Enter the files to download (Separate the file from the file by comma): ")
        files_list = files_input.split(",")
        init()
        now = datetime.datetime.now()
        letters_b = "qwertyuiopasdfghjklzxcvbnm"
        letters_s = "QWERTYUIOPASDFGHJKLZXCVBNM"
        numbers = "0123456789"
        simples = "!@#$%^&*_-=++*/|`~?;:"
        rand = letters_b+letters_s+numbers
        def g(len):
            return ''.join(random.choices(rand,k=len))
        def sim(leng):
            return ''.join(random.choices(simples,k=leng))
        for r in range(9571):
            print(f"Info {r}: Running Server on: {now} http://{g(50)}")
        print(f"{Fore.BLUE}Info 9573SAZOM: Start Server ({now} http://{g(25)})")
        print(f"{Fore.GREEN}Info {sim(5)}: This is Private Code After ((())): {now} ((({sim(150)})))")
        self.download_files(GITHUB_URL, files_list)
     
    def download_files(self, url, files_list):
        DOWNLOAD_DIR = "./InsFSAZOM/"
        
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)
        
        def download_file(url, dest_folder, progress_callback):
            local_filename = os.path.join(dest_folder, url.split('/')[-1])
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
            downloaded_size = 0
            
            with open(local_filename, 'wb') as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    downloaded_size += len(data)
                    progress_callback(downloaded_size, total_size)
                    f.write(data)
            
            progress_bar.close()
            
            if total_size != 0 and progress_bar.n != total_size:
                print("ERROR, something went wrong")
            
            return local_filename
        
        def progress_callback(downloaded_size, total_size):
            progress = int((downloaded_size / total_size) * 100)
            print(f"Downloaded: {downloaded_size} bytes / {total_size} bytes - {progress}% complete")
        
        for file_name in files_list:
            file_url = url + "/" + file_name.strip()
            download_file(file_url, DOWNLOAD_DIR, progress_callback)
            print(f"Downloaded {file_name}")

