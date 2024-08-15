from getExifData import *
from mediaUtils import *
from getVideoData import *
from fileCreator import *
from photoLibrary import PhotoLibrary
from videoLibrary import VideoLibrary

#First open an SSH connection to NAS
print("Have you opened your SSH?")
isOpen = input("Enter 'y' for Yes or 'n' for No:  ")


#Get path to folder in question
if isOpen == "y":
    path = input("Copy path of the photos in question here:")
    if path:
        load_file_libraries(path)
        new_photo_library = PhotoLibrary.photo_library
        new_video_library = VideoLibrary.video_library
        organize_photos(path, new_photo_library, new_video_library)
    else:
        print(f"Sorry, path {path} does not exist or is not accessible")



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