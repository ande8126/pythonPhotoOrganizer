import tkinter as tk
from tkinter import filedialog 

def pick_a_folder_to_organize():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Pick a folder to organize your photos")
    return folder_path 