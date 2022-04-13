from tkinter import *
import sqlite3

root = Tk()
root.title('Contact Book')
root.geometry('700x700')
root.resizable(0, 0)

Label(root, text= 'First Name').place(x=5,y=5)
Label(root, text = 'Last Name').place(x=5,y=25)
Label(root, text= 'Phone').place(x=5,y=45)
Label(root, text= 'Address').place(x=5,y=65)

root.mainloop()