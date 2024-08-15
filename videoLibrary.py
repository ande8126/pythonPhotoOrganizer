from videoData import VideoData

class VideoLibrary:
    video_library = []

    @classmethod
    def add_video_to_library(cls, file_name, date_of_creation, day, month, year, datatype):
        new_video = VideoData(file_name, date_of_creation, day, month, year, datatype)
        cls.video_library.append(new_video)
    
