from tkinter import *
import sqlite3

root = Tk() 
root.title('Contact Book') #Give our program a title
root.geometry('700x700') #Size the window
root.resizable(0, 0) #Restrict user from minimizing or resizing the window

#Add labels telling users what they can enter in
Label(root, text= 'First Name').place(x=5,y=5)
Label(root, text = 'Last Name').place(x=5,y=25)
Label(root, text= 'Phone').place(x=5,y=45)
Label(root, text= 'Address').place(x=5,y=65)

#Add entry boxes and save the entry to a variable
first_name_entry = Entry(root, width=20).place(x=80,y=5)
last_name_entry = Entry(root, width=20).place(x=80,y=25)
phone_entry = Entry(root, width=20).place(x=80,y=45)
address_entry = Entry(root, width=20).place(x=80,y=65)

#Add buttons that will soon have commands
add_button = Button(root, text="Add").place(x=20, y=90)
delete_button = Button(root, text="Delete").place(x=80, y=90)
search_button = Button(root, text="Search").place(x=155, y=90)

#Listbox that will soon store all contact information
info_box = list1 = Listbox(root, height=28, width=70).place(x=35,y=200) 


root.mainloop() #Keep window open until closed
