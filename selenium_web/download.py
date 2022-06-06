from pytube import YouTube
url = ''
yt = YouTube(url)
filters = yt.streams.filter(file_extension='mp4')


stream = yt.streams.get_by_itag(22)
stream.download()