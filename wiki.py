import tkinter
from tkinter import *
import wikipedia as wk
window=Tk()
window.title("my wikipedia")
window.config(bg="black")

f1_heading=Frame(window)
f2_frame=Frame(window)
f3_result=Frame(window)

Label(f1_heading,text="my wikipedia",font=("Arial",30,"bold")).pack(side=TOP)
Label(f2_frame,text="search here",font=("arial",20,"italic"),bg="lightblue").pack(side=LEFT)
Label(f3_result,text="searched results",font=("arial",20,"bold"),bg="lightblue").pack(side=LEFT)

box=Entry(f2_frame,width=40,font=("arial",20,"bold"))
box.pack(side=LEFT,fill=BOTH,expand=5)
box.focus_set()

query=''
text=Text(window,font=("arial",10,"bold"),bg="lightblue",pady=10,padx=50,)

def text_search():
 global query
 query=box.get()
 try:
   text_summary=wk.summary(query)
   text.insert('1.0',text_summary)
 except:
  text.insert('1.0','no results found')

button=Button(f2_frame,text="search",command=text_search,font=("arial",20,"bold"),bg="red",fg="white")
button.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_result.pack(side=TOP,padx=50,pady=20)
text.pack()

window.mainloop()