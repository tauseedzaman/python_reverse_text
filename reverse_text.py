from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import pyperclip as pc 
app = Tk()
app.title("Reverse Text")
app.geometry('700x500+100+100')
app.config(bg="black")
def reverse():
	x = textBox.get(1.0,END)
	if x == '':
		messagebox.showinfo("Stop","Enter some text")
	r_text = x[::-1]
	textBox.delete(1.0,END)
	textBox.insert(END,r_text)
def copy():
	text = textBox.get(1.0,END)
	pc.copy(text)
# title
Label(app,text="Reverse text",bg="black",fg="cyan",font=("times bold ", 30)).place(x=150,y=20)
#text label
Label(app,text="Enter Text",bg="black",fg="cyan",font=("times bold ", 15)).place(x=150,y=150)
#text box
textBox = ScrolledText(app,bg="black",fg="cyan",font=("times bold ", 30),bd=2,relief=GROOVE,width=20,height=5)
Button(app,text="Reverse",bg="green",fg="cyan",font=("times bold ", 20),command=reverse,bd=2,relief=GROOVE,width=5,padx=20	).place(x=150,y=430)
Button(app,text="Copy",bg="green",fg="cyan",font=("times bold ", 20),command=copy,bd=2,relief=GROOVE,width=5,padx=10).place(x=500,y=430)
textBox.place(x=150,y=180)
app.mainloop()