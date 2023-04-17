
'''
Python Program to Create Digital Clock
Author: Dr.Milan Parmar
'''
import socket as s 
from tkinter import *
from tkinter.ttk import *

import tkinter as tk

from time import strftime

root = Tk()

root.title("Digital clock")
my_hostname = s.gethostname()
host = "digikala.ir"
ip = s.gethostbyname(host)

def clock():
    inputtxt = Text(root,height = 20,width = 50)
    


    tick = strftime(f"{ip}")
    label.config(text =tick)



label = Label(root, font = ("segoe", 60), foreground = "yellow", background = "black")

label.pack(anchor= "center")
lbl = tk.Label(root, text = "give me")
lbl.pack()




clock()
mainloop()


