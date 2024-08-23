# pythonPhotoOrganizer

## Works on small, local drives
Go into a photo library, detect existing photos/videos and automatically sort them into the following file structure:
* Year
* Month
* Filetype(Photo and Video)

## Using the app: 
* Add container to Docker with command: docker build -t pythonphotoorganizer .
* Run via Docker with the command: docker run -v /your/filepath/here:/mnt/data/ pythonphotoorganizer

## Next up
* Otherways to deploy this... can this just sit in photo library somewhere and run if it needs to in the background?