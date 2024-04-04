from tkinter import *
a = Tk()
a.title("Calculator" )
input= Entry(a, width=50)
input.grid(row=0, column=0, columnspan=3 ,padx=15,pady=15)

def click(num):
    var = input.get()
    input.delete(0, END)
    input.insert(0, str(var) + str(num))
    return

def add():
    var = input.get()
    global fnum
    fnum = int(var)
    input.delete(0, END)
    return

def equal():
    var =input.get()
    snum = int(var)
    input.delete(0, END)
    input.insert(0, str(fnum + snum))
    return

def ac():
    input.delete(0, END)
    return

b1 =Button(a, text="1", padx=50,pady=25,command=lambda: click(1))
b2 =Button(a, text="2", padx=50,pady=25,command=lambda: click(2))
b3 =Button(a, text="3", padx=50,pady=25,command=lambda: click(3))
b4 =Button(a, text="4", padx=50,pady=25,command=lambda: click(4))
b5 =Button(a, text="5", padx=50,pady=25,command=lambda: click(5))
b6 =Button(a, text="6", padx=50,pady=25,command=lambda: click(6))
b7 =Button(a, text="7", padx=50,pady=25,command=lambda: click(7))
b8 =Button(a, text="8", padx=50,pady=25,command=lambda: click(8))
b9 =Button(a, text="9", padx=50,pady=25,command=lambda: click(9))
b0 =Button(a, text="0", padx=50,pady=25,command=lambda: click(0))
b_add =Button(a, text="+",padx=105,pady=25,command=add)
b_ac =Button(a, text="AC",padx=45,pady=25,command=ac)
b_equal =Button(a, text="=",padx=105,pady=25,command=equal)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b6.grid(row=2, column=0)
b5.grid(row=2, column=1)
b4.grid(row=2, column=2)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b0.grid(row=4, column=0)
b_add.grid(row=4, column=1, columnspan=2)

b_ac.grid(row=5,column=0)
b_equal.grid(row=5, column=1,columnspan=2)

a.mainloop()