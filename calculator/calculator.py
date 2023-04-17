import tkinter as tk
from tkinter import ttk

exp = " "
def press(num):
    global exp
    exp+= str(num)
    equation.set(exp)

def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = " "
    except:
        equation.set("error")
        exp = " "

def clear():
    global exp
    exp = " "
    equation.set(" ")


if __name__ == "__main__":

    dk = tk.Tk()
    dk.title("calculator")
    # dk.iconbitmap()
    # dk.geometry("258*170")
    # dk.maxsize(width=260 , height=170)

    dk.configure(background="black")

equation = tk.StringVar()
dis_entry = ttk.Entry(dk,width=65 , state = "readonly" ,background = "red" ,textvariable = equation)
dis_entry.grid(row =0 , columnspan = 10 ,ipadx =6 ,ipady=8)
dis_entry.focus()

 
# 7 8 9 
btn7 = ttk.Button(dk,text="7",width=10,command=lambda:press(7))
btn7.grid(row=1 ,column=0 ,ipady=5 , ipadx=5)
btn8 = ttk.Button(dk,text="8",width=10,command=lambda:press(8))
btn8.grid(row=1 ,column=1 ,ipady=5 , ipadx=5)
btn9 = ttk.Button(dk,text="9",width=10,command=lambda:press(9))
btn9.grid(row=1 ,column=2 ,ipady=5 , ipadx=5)
# - *
btnmines = ttk.Button(dk,text="-",width=10,command=lambda:press("-"))
btnmines.grid(row=1 ,column=3 ,ipady=5 , ipadx=5)
btnmulti = ttk.Button(dk,text="*",width=10,command=lambda:press("*"))
btnmulti.grid(row=1 ,column=4 ,ipady=5 , ipadx=5)
# 4 5 6
btn4 = ttk.Button(dk,text="4",width=10,command=lambda:press(4))
btn4.grid(row=2 ,column=0 ,ipady=5 , ipadx=5)
btn5 = ttk.Button(dk,text="5",width=10,command=lambda:press(5))
btn5.grid(row=2 ,column=1 ,ipady=5 , ipadx=5)
btn6 = ttk.Button(dk,text="6",width=10,command=lambda:press(6))
btn6.grid(row=2 ,column=2 ,ipady=5 , ipadx=5)
# + /
btnplus = ttk.Button(dk,text="+",width=10,command=lambda:press("+"))
btnplus.grid(row=2 ,column=3 ,ipady=5 , ipadx=5)
btndiv = ttk.Button(dk,text="/",width=10,command=lambda:press("/"))
btndiv.grid(row=2 ,column=4 ,ipady=5 , ipadx=5)
# 1 2 3 
btn1 = ttk.Button(dk,text="1",width=10,command=lambda:press(1))
btn1.grid(row=3 ,column=0 ,ipady=5 , ipadx=5)
btn2 = ttk.Button(dk,text="2",width=10,command=lambda:press(2))
btn2.grid(row=3 ,column=1 ,ipady=5 , ipadx=5)
btn3 = ttk.Button(dk,text="3",width=10,command=lambda:press(3))
btn3.grid(row=3 ,column=2 ,ipady=5 , ipadx=5)

btn0 = ttk.Button(dk,text="0",width=10,command=lambda:press(0))
btn0.grid(row=3 ,column=3 ,ipady=5 , ipadx=5)

btnequal = ttk.Button(dk,text="=",width=10,command=equalpress)
btnequal.grid(row=3 ,column=4 ,ipady=5 , ipadx=5)

btnclr = ttk.Button(dk,text="Clear",width=5 ,command= clear)
btnclr.grid(row=4 ,columnspan = 6 ,ipady=4 ,ipadx = 170)

dk.mainloop()
