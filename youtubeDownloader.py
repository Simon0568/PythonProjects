from pytube import YouTube

videolink = "https://www.youtube.com/watch?v=7BXJIjfJCsA"

yout = YouTube(videolink)

w = yout.streams.get_highest_resolution()

w.download(output_path="C:/Users/simon/OneDrive/Desktop/Python Projects") #the backslashes have to be facing this way, if you put "\" it will just be a normal string but that won't work since for this raw strings are required
print("Download complete..")

#testing what to do when code is changed
