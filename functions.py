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
            for key in keys:
                print(key)
        except Exception as e:
            print(e)

    def input_server_forklist(self):
        try:
            pass
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