from exifData import ExifData

class PhotoLibrary:
    photo_library = []

    @classmethod
    def add_photo_to_library(cls, file_name, date_of_creation, day, month, year, datatype):
        new_photo = ExifData(file_name, date_of_creation, day, month, year, datatype)
        cls.photo_library.append(new_photo)
    
    @classmethod
    def clear_library(self):
        self.photo_library = []
        