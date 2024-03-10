from pytube import YouTube
from moviepy.editor import *
import os

def title_to_filename(title):
    # Remove disallowed characters in filenames
    invalid_chars = "<>:\"/\\|?*"
    for char in invalid_chars:
        title = title.replace(char, '')
    return title

def download_video(url):
    # Download video from YouTube
    video = YouTube(url)
    video_title = title_to_filename(video.title)
    output_path = f"{video_title}.mp3"

    stream = video.streams.get_audio_only()
    download_filename = stream.download(filename=f"{video_title}.mp4")

    # Convert video to mp3
    video_clip = AudioFileClip(download_filename)
    video_clip.write_audiofile(output_path)

    # Remove the original download
    os.remove(download_filename)
    print(f'Download and conversion complete. File saved as {output_path}')

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
