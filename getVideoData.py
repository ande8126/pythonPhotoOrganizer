import os 
import shutil 
from datetime import datetime 
from pymediainfo import MediaInfo
from videoLibrary import VideoLibrary


def get_video_data(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None
    
    try:
        video = MediaInfo.parse(path)
        if video: 
            for track in video.tracks:
                if track.track_type == "General":
                    date_time = track.tagged_date
                    return date_time
        return None
    except Exception as e:
        print(f"Error with file {path}: {e}")
        return None