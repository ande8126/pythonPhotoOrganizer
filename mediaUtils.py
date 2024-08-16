import os

def get_files_names(path):
    file_names = []
    for root, _, files in os.walk(path):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names
    #file_names = os.listdir(path)
    #return[file for file in file_names if os.path.isfile(os.path.join(path, file))]

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

async def get_target_path(new_path, file_name):
    new_file_name = file_name
    count = 1
    #Hangs on this, needs to change:
    while os.path.exists(os.path.join(new_path, file_name)):
        count += 1
        
    new_file_name = f"{file_name}_{count}"
    return os.path.join(new_path, new_file_name)
