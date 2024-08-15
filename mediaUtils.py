import os

def get_files_names(path):
    file_names = os.listdir(path)
    return[file for file in file_names if os.path.isfile(os.path.join(path, file))]

def get_values_from_photo_datetime(date_string):
    if date_string:
        date_part = date_string.split(" ")[0]
        year, month, day = date_part.split(":")
        return int(year), int(month), int(day)
    return None, None, None

def get_values_from_video_datetime(date_string):
    if date_string:
        date_part = date_string.split(" ")[0]
        year, month, day = date_part.split("-")
        return int(year), int(month), int(day)
    return None, None, None