# pip install pytube
import pytube

url = input("Enter Your YouTube link...\n")
video = pytube.YouTube(url)
stream = video.streams.get_by_itag(22) # 22 is for Downloading 720p videos only.
print("DOWNLOADING YOUR VIDEO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
stream.download(filename=f"{input('Enter your file name... ')}")
print("DONE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

'''for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print(stream)
'''