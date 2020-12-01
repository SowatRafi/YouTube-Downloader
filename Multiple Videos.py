# pip install pytube
import pytube

video_list = []
print("Habibi, please type 'STOP, HABIBI.' to terminate.")
while True:
    url = input("Enter Your YouTube Link, Habibi ......... \n")
    if url == 'STOP, HABIBI.':
        break
    video_list.append(url)

for i, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(22)  # For 720p supported videos only
    print(f'DOWNLOADING VIDEO - {i}')
    stream.download(filename=f"{input('Enter your file name Habibi... ')}")
    print("DONE HABIBI >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")