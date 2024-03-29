import tkinter
from tkinter import*
from tkinter import messagebox
import pyspeedtest

def one():
 speed=pyspeedtest.SpeedTest("www.google.com")
 a1=(str(speed.download())+"[bytes per second]")
 messagebox.showinfo("your download speed",a1)
box = Tk()
box.title("INTERNET SPEED CHECKER")
box.config(bg="lightgreen")
box.geometry("500x200")
label=Label(box,text="internet speed checker",font=("roman",30,"bold"),bg="pink").pack()
button=Button(box,text="click!",font=("roman",20,"bold"),bg="blue",height=1,width=10,command=one).pack()

box.mainloop()
