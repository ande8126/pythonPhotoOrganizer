import os 
import shutil 
from datetime import datetime 
from pymediainfo import MediaInfo
from videoLibrary import VideoLibrary


def get_video_data(path):
    video = MediaInfo.parse(path)
    if video: 
        for track in video.tracks:
            if track.track_type == "General":
                date_time = track.tagged_date
                print(date_time)
                return date_time
    return None