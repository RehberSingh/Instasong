from pytube import YouTube
import os
from pydub import AudioSegment
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import uuid

def audio_processing(f):
    try:
        video_link = f
        video = YouTube(video_link)
        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download()
        required_video_file = audio.default_filename
        starttime = int((video.length)/2)
        print(starttime)
        endtime = int(starttime+5)
        ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str('result')+".mp4")

        input_file = 'result.mp4'
        output_file = str(uuid.uuid4())
        sound = AudioSegment.from_file(input_file , format="mp4")
        sound.export(output_file, format="wav")
        os.remove("result.mp4")
        os.remove(required_video_file)
        return output_file
    except:
        return("Not Found")


'''https://youtube.com/shorts/t0MFoGKC9PA?feature=share'''