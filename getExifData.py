import os 
import shutil 
from datetime import datetime 
from PIL import Image 
from PIL.ExifTags import TAGS
from photoLibrary import PhotoLibrary

def get_files_names(path):
    file_names = os.listdir(path)
    return[file for file in file_names if os.path.isfile(os.path.join(path, file))]

def get_values_from_datetime(date_string):
    if date_string:
        date_part = date_string.split(" ")[0]
        year, month, day = date_part.split(":")
        return int(year), int(month), int(day)
    return None, None, None

def get_exif_data(path):
    image = Image.open(path)
    exif_data = image._getexif()
    if exif_data:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'DateTimeOriginal':
                return value
    return None

def get_datatype(file_name):
    _, file_extension = os.path.splitext(file_name)
    file_extension.lower()
    print(file_extension)
    if file_extension == ".jpg":
        return "photo"
    if file_extension == ".jpeg":
        return "photo"
    if file_extension == ".jfif":
        return "photo"
    if file_extension == ".pjpeg":
        return "photo"
    if file_extension == ".pjp":
        return "photo"
    if file_extension == ".pnp":
        return "photo"
    if file_extension == ".svg":
        return "photo"
    if file_extension == ".webp":
        return "photo"
    if file_extension == ".gif":
        return "photo"
    if file_extension == ".mov":
        return "video"
    if file_extension == ".mp4":
        return "video"
    if file_extension == ".avi":
        return "video"
    if file_extension == ".wmv":
        return "video"
    if file_extension == ".webm":
        return "video"
    if file_extension == ".hvec":
        return "video"
    return None
    


