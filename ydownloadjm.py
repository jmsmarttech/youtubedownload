from pytube import YouTube
link = input("URL do youtube")
vidio = YouTube(link)
stream = video.streams.GET_HIGHEST_resolution()
stream.download()
