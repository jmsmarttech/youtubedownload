from pytube import YouTube
link = input("URL")
vidio = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
