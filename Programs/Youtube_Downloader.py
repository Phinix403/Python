# pip install pytube - to Download Youtube Videos

from pytube import YouTube

link = input("Enter an Link: ")

try:
    yt = YouTube(link)
except:
    print("Enter an Valid Link!")


mp4file = yt.streams.filter(file_extension='mp4')

try:
    print("Starting...")
    yt.streams.get_highest_resolution().download()
    print('Task Completed')

except:
    print("Error!!")