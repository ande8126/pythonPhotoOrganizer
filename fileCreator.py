import os
import shutil
from getExifData import *
from mediaUtils import *
from getVideoData import *
from photoLibrary import PhotoLibrary
from videoLibrary import VideoLibrary

#This method will compile all the various
#video and photo meta data in the filepath you entered
#in the else clause we print to console all files skipped by the program

def load_file_libraries(path):
        file_names = get_files_names(path)
        for file in file_names:
            print(f"fileName: {file}")
            file_path = (f"{path}/{file}")
            datatype = get_datatype(file)
            print(datatype)
            if datatype == "photo": 
                new_datetime = get_exif_data(file_path)
                year, month, day = get_values_from_photo_datetime(new_datetime)
                PhotoLibrary.add_photo_to_library(file, new_datetime, day, month, year, datatype)
            if datatype == "video":
                new_datetime = get_video_data(file_path)
                year, month, day = get_values_from_video_datetime(new_datetime)
                VideoLibrary.add_video_to_library(file, new_datetime, day, month, year, datatype)
                print(new_datetime, year, month, day)
            else:
                print(f"file {file} does not have a recognized media format")

def organize_photos(path, incoming_photo_library, incoming_video_library):
    for photo in incoming_photo_library:
        file_name = photo.file_name
        year_folder = str(photo.year)
        month_folder = str(photo.month)
        datatype_folder = "Photos"

        target_directory = os.path.join(path, year_folder, month_folder, datatype_folder)

        os.makedirs(target_directory, exist_ok=True)

        original_file_path = os.path.join(path, file_name)
        target_path = os.path.join(target_directory)

        if os.path.exists(original_file_path):
            shutil.move(original_file_path, target_path)
            print(f"Moved {file_name} to {target_path}")
        else:
            print(f"File not found: {original_file_path}")

    for video in incoming_video_library:
        file_name = video.file_name
        year_folder = str(video.year)
        month_folder = str(video.month)
        datatype_folder = "Videos"

        target_directory = os.path.join(path, year_folder, month_folder, datatype_folder)

        os.makedirs(target_directory, exist_ok=True)

        original_file_path = os.path.join(path, file_name)
        target_path = os.path.join(target_directory)

        if os.path.exists(original_file_path):
            shutil.move(original_file_path, target_path)
            print(f"Moved {file_name} to {target_path}")
        else:
            print(f"File not found: {original_file_path}")         