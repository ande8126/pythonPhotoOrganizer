from getExifData import *
from photoLibrary import PhotoLibrary

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
                year, month, day = get_values_from_datetime(new_datetime)
                PhotoLibrary.add_photo_to_library(file, new_datetime, day, month, year, datatype)

new_photo_library = PhotoLibrary.photo_library

for photo in new_photo_library:
    print(photo)



#Use the data to determine the need for folder structure

#Goal is to create folder structure that accounts for
##Year
##Month
##Video Or Photo (one folder for each)

#After folders are made, move photos into folders