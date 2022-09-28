from ast import pattern
import fnmatch
import tkinter as tk
import os
from tracemalloc import start
from pygame import mixer


canvas = tk.Tk()
canvas.title("Terraria Music Player")
canvas.geometry("600x800")
canvas.config(bg="black")
canvas.resizable(False, False)

photo = tk.PhotoImage(file = "icons/pic.png")

canvas.iconphoto(False, photo)

path = "tracks"
ext = "*.wav"

mixer.init()

play_img = tk.PhotoImage(file = "icons\play.png")
pause_img = tk.PhotoImage(file = "icons\pause.png")

def start():
    mixer.music.load(path + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()

listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('poppins', 14))
listbox.pack(padx = 15, pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = "center")

playButton = tk.Button(canvas, text = "Play", image = play_img, bg = "white", borderwidth = 0, command = start)
playButton.pack(pady = 15, in_ = top, side = "left")

pauseButton = tk.Button(canvas, text = "Play", image = pause_img, bg = "white", borderwidth = 0, command = stop)
pauseButton.pack(pady = 15, in_ = top, side = "left")


for root, dirs, files in os.walk(path):
    for filename in fnmatch.filter(files, ext):
        listbox.insert('end', filename)

canvas.mainloop()