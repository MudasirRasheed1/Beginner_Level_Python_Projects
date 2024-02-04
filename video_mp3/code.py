import os #operating system utilities
import shutil #shell utilities

from pytube import YouTube #brings in YouTube class from pytube module

def download_video(url):
    yt = YouTube(url) #creates a object of YouTube class
    file = yt.streams.get_audio_only() #gets the first stream of the video
    file.download() #downloads the file to the current directory with default name

    mp4_name = file.default_filename #gets the name of the file 
    mp3_name = mp4_name.replace('mp4', 'mp3') #replaces string mp4 with mp3
    os.rename(mp4_name, mp3_name) #renames the file in local directory 


    shutil.move(mp3_name, 'audio') #moves the file from one location to another location

def main():
    try:
        intput_url = input('Enter the URL of the video you want to download: ')
        download_video(intput_url)
        print('Download completed successfully!')
    except Exception as e:
        print(e)
        print('Download failed!')
if __name__ == '__main__':
    main()



