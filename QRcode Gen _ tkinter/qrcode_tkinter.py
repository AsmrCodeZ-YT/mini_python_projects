import pyqrcode
from  tkinter.ttk import *
from tkinter import *

def GEN():
    num_scale = select_box.get()
    data =  name_var.get()

    num_scale = int(num_scale)

    qr = pyqrcode.create(data)
    qr.png(f"{data}_{num_scale}x{num_scale}.png" ,num_scale)
    print(data, num_scale)



root = Tk()
root.title("QR code Gen")
root.geometry("320x45")
root.minsize(320 ,45)
root.maxsize(320,45)
root.configure(background="black")
######################################
name_var = StringVar()
select_box = StringVar()




name_entry = Entry(root,textvariable=name_var ,font=("Arial",15),
                   background="black",fg="yellow")
name_entry.grid(row=1 ,column=0,padx=5,pady=5)

gen_btn = Button(root,text="Gen",command=GEN,fg="yellow",background="black",
                 font=("Arial",13,"normal"))
gen_btn.grid(row=1,column=1)


num = Combobox(root,width=3,textvariable=select_box,background="black")
num["values"] = (" 1",
                 " 2",
                 " 3",
                 " 4",
                 " 5",
                 " 6",
                 " 7",
                 " 8",
                 " 9",
                 " 10")

num.grid(row=1,column=2,padx=5,pady=5)
num.current()
root.mainloop()




