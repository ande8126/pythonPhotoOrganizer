from getExifData import *
from mediaUtils import *
from getVideoData import *
from photoLibrary import PhotoLibrary
from videoLibrary import VideoLibrary

#First open an SSH connection to NAS
print("Have you opened your SSH?")
isOpen = input("Enter 'y' for Yes or 'n' for No:  ")


#Get path to folder in question
if isOpen == "y":
    path = input("Copy path of the photos in question here:")
    if path:
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
        print(f"Sorry, path {path} does not exist or is not accessible")

new_photo_library = PhotoLibrary.photo_library
new_video_library = VideoLibrary.video_library

for photo in new_photo_library:
    print(photo.file_name)
    print(photo.year)
    print(photo.month)
    print(photo.day)

for video in new_video_library:
    print(video.file_name)
    print(video.year)
    print(video.month)
    print(video.day)


#Use the data to determine the need for folder structure

#Goal is to create folder structure that accounts for
##Year
##Month
##Video Or Photo (one folder for each)

#After folders are made, move photos into folders