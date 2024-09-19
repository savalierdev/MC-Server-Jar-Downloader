import requests
import tkinter as tk
from tkinter import filedialog

file_name = "server.jar"

class Service:
    def __init__(self):
        pass

    def server_forklists(self):
        try:
            response = requests.get("https://mcutils.com/api/server-jars")
            forklist = response.json()
            keys = [item['name'] for item in forklist if 'name' in item]
            return keys
        except Exception as e:
            print(e)

    def print_server_forklist(self):
        try:
            keys = self.server_forklists()
            for index, key in enumerate(keys, start=1):
                print(f"{index}. {key}")
            self.input_server_forklist()
        except Exception as e:
            print(e)

    def input_server_forklist(self):
        try:
            while True:
                try:
                    self.selection = int(input("Select Server Fork: "))
                    if 1 <= self.selection <= len(self.server_forklists()):
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(self.server_forklists())}.")
                except ValueError:
                    print(f"Invalid input. Please enter a number between 1 and {len(self.server_forklists())}.")
        except Exception as e:
            pass

class FileOperations:
    def __init__(self):
        self.file_name = file_name

    def select_folder(self):
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        print('Folder selected:', folder_selected)
        return folder_selected
    
    def download_file(self,file_name):
        pass