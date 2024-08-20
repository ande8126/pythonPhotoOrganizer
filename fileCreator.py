import os
import asyncio
import aiofiles
import tempfile
import shutil
from getExifData import *
from mediaUtils import *
from getVideoData import *
from photoLibrary import PhotoLibrary
from videoLibrary import VideoLibrary

#This method will compile all the various
#video and photo meta data in the filepath you entered
#in the else clause we print to console all files skipped by the program

async def load_file_libraries(path, file_names):

    tasks = [] #for async

    for file in file_names:
        
        #file_path = (f"{path}/{file}")
        file_path = file
        datatype = get_datatype(file)
        print(datatype)

        if datatype == "photo": 
            tasks.append(add_photo(file_path, file, datatype))
        if datatype == "video":
            tasks.append(add_video(file_path, file, datatype))
        else:
                print(f"file {file} does not have a recognized media format")
    
    await asyncio.gather(*tasks)

async def organize_photos(path, incoming_photo_library, incoming_video_library):
    tasks = []

    for photo in incoming_photo_library:
        tasks.append(move_file(photo.file_name, photo.year, photo.month, "Photos", path))

    for video in incoming_video_library:
        tasks.append(move_file(video.file_name, video.year, video.month, "Videos", path)) 

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

    original_file_path = file_name
    just_name = os.path.basename(file_name)
    #target_path = await get_target_path(target_directory, just_name) -- this needs work
    target_path = os.path.join(target_directory, just_name)

    #Move files to new path (whole)
    if os.path.exists(original_file_path):
        shutil.move(original_file_path, target_path)

    ##TODO: Figure out chunking. Failed in some tests, too risky
    # #use temp file as a shell for each file to avoid corrupted files in case this breaks during the run
    # temp_file_path = None
    # if os.path.exists(original_file_path):
    #     async with aiofiles.open(original_file_path, 'rb') as src_file:
    #         temp_file_fd, temp_file_path = tempfile.mkstemp(dir=target_directory)
    #         async with aiofiles.open(temp_file_fd, 'wb') as dest_file:
    #             while True:
    #                 chunk = await src_file.read(1024 * 1024) #read in chunks
    #                 if not chunk:
    #                     break
    #                 await dest_file.write(chunk)

    #     #Update temp file to the final target file
    #     os.rename(temp_file_path, target_path)
    #     os.remove(original_file_path)

        print(f"Moved {file_name} to {target_path}")
    else:
        print(f"File not found: {original_file_path}")  