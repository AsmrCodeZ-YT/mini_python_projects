import socket as s 
from tkinter.ttk import *
from tkinter import *
import tkinter as tk


def IP():
        
    host = name_entry.get()
    ip = s.gethostbyname(host)
    label.config(text=ip)
    name_var.set("")






root = tk.Tk()
root.configure(background="black")
root.title("IP Address ")

##########
name_var = tk.StringVar()

label = Label(root, font=("Arial",60),foreground="yellow",background="black")
label.pack(anchor="center")
label.grid(row=0)



ip = s.gethostbyname("0.0.0.0")
label.config(text=ip)


#name_var


name_entry = tk.Entry(root ,textvariable= name_var ,font=("Arial",15),
                      background="black",fg="yellow",width="20")
name_entry.grid(row=1,column=0)


sub_btn = tk.Button(root,text="IP",command=IP,fg="yellow",background="black",
                    font=("Arial",15,"normal"))
sub_btn.grid(row=1,column=1)






root.mainloop()