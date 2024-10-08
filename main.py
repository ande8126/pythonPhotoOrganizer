import asyncio
from getExifData import *
from mediaUtils import *
from getVideoData import *
from fileCreator import *
from folderSelect import *
from photoLibrary import PhotoLibrary
from videoLibrary import VideoLibrary

async def main():
    #I had this initially thinking I'd have to run this
    #through an SSH connection to my NAS, not sure thats the case anymore

    #First open an SSH connection to NAS
    # print("Have you opened your SSH?")
    #isOpen = input("Enter 'y' for Yes or 'n' for No:  ")

    #Get path to folder in question
    #if isOpen == "y":
    #path = input("Copy path of the photos in question here:")
    path = "/mnt/data"
    
    if path:
        #Once you get the path, first load in file names
        print("Loading files from original paths...")
        file_names = get_files_names(path)
        total_files = len(file_names)
        moved_files = 0
        print(f"Loaded {total_files} files to move...")
        batch_size = 1000


        for i in range(0, len(file_names), batch_size):
            file_batch = file_names[i:i + batch_size]
            files_to_move = len(file_batch)

            await load_file_libraries(path, file_batch)
            batch_photo_library = PhotoLibrary.photo_library
            batch_video_library = VideoLibrary.video_library
            #This method actually moves the files in question
            #While also creating Year>Month>[Photos, Videos] folders as needed
            await organize_photos(path, batch_photo_library, batch_video_library)
            PhotoLibrary.clear_library()
            VideoLibrary.clear_library()
            moved_files += files_to_move
            print(f"\rMoving files: {moved_files}/{total_files} completed", end="")

        print(f"\n\nFinished successfully")
    else:
        exit(1)

if __name__ == "__main__":
    asyncio.run(main())


