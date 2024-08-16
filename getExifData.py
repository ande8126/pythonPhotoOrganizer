import os 
from datetime import datetime 
from PIL import Image 
from PIL.ExifTags import TAGS
from photoLibrary import PhotoLibrary

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
    _, raw_file_extension = os.path.splitext(file_name)
    file_extension = raw_file_extension.lower()
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
    #if file_extension == ".heic": --Python doesn't like these, can I convert?
    #    return "photo"
    if file_extension == ".gif":
        return "photo"
    if file_extension == ".png":
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
    


