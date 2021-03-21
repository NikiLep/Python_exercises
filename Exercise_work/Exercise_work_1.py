# File:         Ex8_5
# Author:       Niki Leppänen
# Description:  Simple GUI with tkinter, main screen has buttons that opens different applications/games
#               (alarm clock, card games, dice roll, ect.)

from tkinter import *
from tkinter.ttk import *
import requests
from PIL import Image, ImageTk
from Exercise_work.paint import Paint

# creates a Tk() object and sets the geometry of main root window
root = Tk()
root.geometry('1280x800')

label = Label(root,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# paint window on button click
btn = Button(root,
             text="PAINT")
btn.bind("<Button>", lambda e: Paint(root))
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()


root.mainloop()