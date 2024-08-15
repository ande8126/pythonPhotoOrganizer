from getExifData import *

#First open an SSH connection to NAS
print("Have you opened your SSH?")
isOpen = input("Enter 'y' for Yes or 'n' for No:  ")


#Get path to folder in question
if isOpen == "y":
    path = input("Copy path of the photos in question here:")
    if path:
        get_exif_data(path)


#Then, get data for photos 

#Use the data to determine the need for folder structure

#Goal is to create folder structure that accounts for
##Year
##Month
##Video Or Photo (one folder for each)

#After folders are made, move photos into folders