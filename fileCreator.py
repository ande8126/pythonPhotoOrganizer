import os
import shutil
import asyncio
import aiofiles
from getExifData import *
from mediaUtils import *
from getVideoData import *
from photoLibrary import PhotoLibrary
from videoLibrary import VideoLibrary

#This method will compile all the various
#video and photo meta data in the filepath you entered
#in the else clause we print to console all files skipped by the program

async def load_file_libraries(path):
    file_names = get_files_names(path)
    tasks = [] #for async

    for file in file_names:
        print(f"fileName: {file}")
        file_path = (f"{path}/{file}")
        datatype = get_datatype(file)

        if datatype == "photo": 
            tasks.append(add_photo(file_path, file, datatype))
            #new_datetime = get_exif_data(file_path)
            #year, month, day = get_values_from_photo_datetime(new_datetime)
            #PhotoLibrary.add_photo_to_library(file, new_datetime, day, month, year, datatype)
        if datatype == "video":
            tasks.append(add_video(file_path, file, datatype))
            #new_datetime = get_video_data(file_path)
            #year, month, day = get_values_from_video_datetime(new_datetime)
            #VideoLibrary.add_video_to_library(file, new_datetime, day, month, year, datatype)
            #print(new_datetime, year, month, day)
        else:
                print(f"file {file} does not have a recognized media format")
    
    await asyncio.gather(*tasks)

async def organize_photos(path, incoming_photo_library, incoming_video_library):
    tasks = []

    for photo in incoming_photo_library:
        tasks.append(move_file(photo.file_name, photo.year, photo.month, "Photos", path))
        # file_name = photo.file_name
        # year_folder = str(photo.year)
        # month_folder = str(photo.month)
        # datatype_folder = "Photos"

        # target_directory = os.path.join(path, year_folder, month_folder, datatype_folder)

        # os.makedirs(target_directory, exist_ok=True)

        # original_file_path = os.path.join(path, file_name)
        # target_path = os.path.join(target_directory)

        # if os.path.exists(original_file_path):
        #     shutil.move(original_file_path, target_path)
        #     print(f"Moved {file_name} to {target_path}")
        # else:
        #     print(f"File not found: {original_file_path}")

    for video in incoming_video_library:
        tasks.append(move_file(video.file_name, video.year, video.month, "Videos", path))
        # file_name = video.file_name
        # year_folder = str(video.year)
        # month_folder = str(video.month)
        # datatype_folder = "Videos"

        # target_directory = os.path.join(path, year_folder, month_folder, datatype_folder)

        # os.makedirs(target_directory, exist_ok=True)

        # original_file_path = os.path.join(path, file_name)
        # target_path = os.path.join(target_directory)

        # if os.path.exists(original_file_path):
        #     shutil.move(original_file_path, target_path)
        #     print(f"Moved {file_name} to {target_path}")
        # else:
        #     print(f"File not found: {original_file_path}")  

    await asyncio.gather(*tasks)

async def add_photo(file_path, file_name, datatype):
    new_datetime = get_exif_data(file_path)
    year, month, day = get_values_from_photo_datetime(new_datetime)
    PhotoLibrary.add_photo_to_library(file_name, new_datetime, day, month, year, datatype)

async def add_video(file_path, file_name, datatype):
    new_datetime = get_video_data(file_path)
    year, month, day = get_values_from_video_datetime(new_datetime)
    VideoLibrary.add_video_to_library(file_name, new_datetime, day, month, year, datatype)
    print(new_datetime, year, month, day)

async def move_file(file_name, year, month, datatype_folder, base_path):
    year_folder = str(year)
    month_folder = str(month)
    target_directory = os.path.join(base_path, year_folder, month_folder, datatype_folder)

    os.makedirs(target_directory, exist_ok=True)

    original_file_path = os.path.join(base_path, file_name)
    target_path = os.path.join(target_directory, file_name)

    if os.path.exists(original_file_path):
        async with aiofiles.open(original_file_path, 'rb') as src_file:
            async with aiofiles.open(target_path, 'wb') as dest_file:
                while True:
                    chunk = await src_file.read(1024 * 1024) #read in chunks
                    if not chunk:
                        break
                    await dest_file.write(chunk)
        os.remove(original_file_path)
        print(f"Moved {file_name} to {target_path}")
    else:
        print(f"File not found: {original_file_path}")  