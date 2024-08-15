from exifData import ExifData

class PhotoLibrary:
    photo_library = []

    @classmethod
    def add_photo_to_library(cls, location, date_of_creation, datatype):
        new_photo = ExifData(location, date_of_creation, datatype)
        cls.photo_library.append(new_photo)
    
