import pytube

url = input("Enter Your YouTube Link, Habibi ......... (Only 720p) \n")
playlist = pytube.Playlist(url)

for url in playlist:
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(22)
    stream.download(output_path=f"{input('Enter your file location Habibi... ')}")