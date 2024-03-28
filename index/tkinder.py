""""
from tkinter import *
from tkinter import messagebox
top= Tk ()
top.geometry("200x100")

def fun():
    messagebox.showinfo("Hello","Red Button Clicked")
def blue():
    messagebox.showinfo("Hello","Blue Button Clicked")
def green():
    messagebox.showinfo("Hello","Green Button Clicked")
def yellow():
    messagebox.showinfo("Hello","Yellow Button Clicked")

b1= Button(top, text="red",command = fun,activeforeground="red", activebackground="pink",pady=10)

b2= Button(top, text="blue",command = blue,activeforeground="blue", activebackground="skyblue",pady=10)

b3=Button(top, text="green",command = green,activeforeground="green", activebackground="lightgreen",pady=10)

b4=Button(top, text="Yellow",command = yellow,activeforeground="gold", activebackground="yellow",pady=10)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

top.mainloop()
"""
"""
from tkinter import*
top=Tk()
top.geometry("200x200")
c= Canvas(top, bg="pink",height="200")
c.pack()
top.mainloop()
"""
"""
from tkinter  import*
top=Tk()
top.geometry("200x200")

checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()

chkbtn1=Checkbutton(top, text="C", variable=checkvar1, onvalue=1, offvalue=0,height=2, width=10)
chkbtn2=Checkbutton(top, text="C++", variable=checkvar2, onvalue=1, offvalue=0,height=2, width=10)
chkbtn3=Checkbutton(top, text="Java", variable=checkvar3, onvalue=1, offvalue=0,height=2, width=10)

chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

top.mainloop()
"""
"""
from tkinter import*
top=Tk()
top.geometry("400x250")

name=Label(top, text="Name").place(x=40,y=50)
email=Label(top, text="E-mail").place(x=40,y=90)
passward=Label(top, text="Passward").place(x=40,y=130)

sbmitbtn=Button(top, text="Submit",activebackground="lightgreen", activeforeground="blue").place(x=40,y=170)

e1=Entry(top).place(x=100,y=50)
e2=Entry(top).place(x=100,y=90)
e3=Entry(top).place(x=100,y=130)
top.mainloop()
"""
"""
import tkinter as tk
from functools import partial

def call_result(label_result, n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label_result.config(text="Result= %d"% result)
    return

root=tk.Tk()
root.geometry("400x200+100+200")

root.title("Calculator")

number1=tk.StringVar()
number2=tk.StringVar()

labelNum1=tk.Label(root,text="A").grid(row=1,column=0)
labelNum2=tk.Label(root,text="B").grid(row=2,column=0)

labelResult=tk.Label(root)
labelResult.grid(row=7,column=2)

entryNum1=tk.Entry(root, textvariable=number1).grid(row=1,column=2)
entryNum2=tk.Entry(root, textvariable=number2).grid(row=2,column=2)
call_result=partial(call_result,labelResult,number1,number2)
buttonCal=tk.Button(root,text="Calculate",command=call_result).grid(row=3,column=0)

root.mainloop()
"""
"""
from tkinter import*
top= Tk()
top.geometry("140x100")
frame=Frame(top)
frame.pack()

leftframe=Frame(top)
leftframe.pack(side=LEFT)

rightframe=Frame(top)
rightframe.pack(side=RIGHT)

btn1=Button(frame,text="Submit", fg="red",activebackground="red")
btn1.pack(side=LEFT)
btn2=Button(frame,text="Remove", fg="brown",activebackground="brown")
btn2.pack(side=RIGHT)
btn3=Button(frame,text="Add", fg="blue",activebackground="blue")
btn3.pack(side=LEFT)
btn4=Button(frame,text="Modify", fg="black",activebackground="White")
btn4.pack(side=RIGHT)
top.mainloop()
"""
"""
from  tkinter import*
top=Tk()
top.geometry("200x250")

menubutton=Menubutton(top, text="Language",relief=FLAT)
menubutton.grid()

menubutton.menu=Menu(menubutton)
menubutton["menu"]=menubutton.menu

menubutton.menu.add_checkbutton(label="Tamil",variable=IntVar())
menubutton.menu.add_checkbutton(label="Englih", variable=IntVar())
menubutton.pack()
top.mainloop()
"""
"""
from tkinter import Toplevel, Button, Tk, Menu
top=Tk()
menubar=Menu(top)
file=Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="open")
file.add_command(label="save")
file.add_command(label="save as...")
file.add_command(label="close")

file.add_separator()
file.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File",menu=file)

edit=Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()

edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)
help=Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)

top.config(menu=menubar)
top.mainloop()
"""
"""
from tkinter import*
root=Tk()
root.geometry("200x200")
def open():
    top=Toplevel(root)
    top.mainloop()
btn=Button(root, text="open", command=open)
btn.place(x=75,y=50)
root.mainloop()
"""
"""
from tkinter import*
def add():
    a=int(e1.get())
    b=int(e2.get())
    leftdata=str(a+b)
    left.insert(1,leftdata)

w1=PanedWindow()
w1.pack(fill = BOTH, expand=1)

left=Entry(w1,bd=5)
w1.add(left)

w2=PanedWindow(w1, orient=VERTICAL)
w1.add(w2)

e1=Entry(w2)
e2=Entry(w2)

w2.add(e1)
w2.add(e2)

bottam=Button(w2, text="Add",command=add)
w2.add(bottam)

mainloop()
"""
"""
from tkinter import*
top= Tk()
top.geometry("300x200")

labelframe1= LabelFrame(top, text="Place the Commands")
labelframe1.pack(fill="both", expand="yes")

toplabel=Label(labelframe1, text="Place to put the Positive Command")
toplabel.pack()

labelframe2= LabelFrame(top, text="Place the Negative Comments")
labelframe2.pack(fill="both",expand="yes")

bottomlabel=Label(labelframe2, text="Place to put the Negative Command")
bottomlabel.pack()

top.mainloop()
"""
"""
Tkinter messagebox
from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("100x100")
messagebox.showinfo("information","Information")
top.mainloop()
"""
"""
from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("100x100")
messagebox.showinfo("Confirm","Are you sure happy?")
top.mainloop()
"""
"""
from tkinter import*
top=Tk()
top.geometry("200x200")
spin=Spinbox(top, from_=0, to=25)
spin.pack()
top.mainloop()
"""
from tkinter import*
def select():
    sel="Value="+str(v.get())
    Label.config(text = sel)
    top=Tk()
    top.geometry("200x100")
    v=DoubleVar()
    scale=Scale(top,variable=v,from_=1,to=50,orient=HORIZONTAL)
    scale.pack(anchor=CENTER)
    btn=Button(top,text="Value",command=select)
    btn.pack(anchor=CENTER)
    label=Label(top)
    label.pack()
    top.mainloop()