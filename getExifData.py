import os 
import shutil 
from datetime import datetime 
from PIL import Image 
from PIL.ExifTags import TAGS
from photoLibrary import PhotoLibrary

def get_exif_data(path):
    image = Image.open(path)
    exif_data = image._getexif()
    if exif_data:
        for tag, value in exif_data.items():
            print(f"tag: {tag} | value: {value}")
    return None
