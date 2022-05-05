from tkinter import *
import sqlite3
import re
from tkinter import messagebox

class Database:
    """Class that will add/delete/search inside the table"""
    def __init__(self):
        """purpose of __init__() is to initialize cursor and connection to database using sqlite3 and create our table if it does not exist
        
        Driver: Shams
        Navigator: Moyukh"""
        self.conn = sqlite3.connect('contacts_database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (first_name TEXT, last_name TEXT, address TEXT, phone_number INTEGER)")
        self.conn.commit()
    
    def add_to_database(self, first_name, last_name, address, phone):
        """Function that will take in passed in first_name, last_name, address, phone and run the INSERT SQL command to add the contact into the database.
        
        Args: 
        first_name(string): first name of contact
        last_name(string): last name of contact
        address(string): address of contact
        phone(int): phone number of contact
        
        Driver: Moyukh
        Navigator: Omar"""

        self.cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", (first_name, last_name, address, phone,))
        self.conn.commit()

        self.cursor.execute("SELECT * FROM contacts")
        self.conn.commit
        return self.cursor.fetchall()
    
    def delete_from_database(self, phone):
        """Function that will delete records by phone number since every contact has a unique phone number.
        Meanwhile, values such as first names, last names, and addresses may be shared and deleting records
        by those values may unintentioanlly delete multiple records
        
        Args:
        phone(int): phone number that will be passed in to the SQL command that deletes a contact by the phone number
        
        Driver: Shams
        Navigator: Omar"""
        self.cursor.execute("DELETE FROM contacts WHERE phone_number=?", (phone,))
        self.conn.commit()
    
    def search_in_database(self, first_name, last_name, address, phone):
        """Function that will search for records by passed in parameters
        
        Args:
        first_name(string): first name of contact
        last_name(string): last name of contact
        address(string): address of contact
        phone(int): phone number of contact
        
        Driver: Moyukh
        Navigator: Shams"""
        self.cursor.execute("SELECT * FROM contacts WHERE first_name=? OR last_name=? OR address=? OR phone_number=?",(first_name, last_name, address, phone,))
        self.conn.commit
        return self.cursor.fetchall()
    
    def select_all(self):
        """Function that runs SQL code that selects all elements inside of contact table.
        
        Driver: Omar
        Navigator: Shams"""
        self.cursor.execute("SELECT * FROM contacts")
        self.conn.commit
        return self.cursor.fetchall()

database = Database()


def add_contact():
    """Purpose of add_contact is to get the value in each entry box and pass it into the database add_to_database function so the contact is added to the database
    
    Driver: Moyukh
    Navigator: Shams"""
    if len(phone_number.get()) != 10:
        messagebox.showinfo('Error', 'Please enter a 10-digit phone number.')
        phone_entry.delete(0, END)
    else:
        database.add_to_database(first_name.get(), last_name.get(), address.get(), phone_number.get()) #passes the entry box values into the database function
        info_box.delete(0, END)#empties the listbox

    for contact in database.select_all(): #Adds contact to the listbox
        info_box.insert(END, contact)

def get_selected(event):
    """Purpose of get selected is to get the value linked to the users cursor selection and pass it into the all_elements entry box.
    
    Driver: Shams
    Navigator: Moyukh"""
    widget = event.widget
    index = int(widget.curselection()[0])
    value = widget.get(index)
    all_elements.set(value)

def view_all():
    """Purpose of view_all is to print all contacts from the database into the listbox
    
    Driver: Omar
    Navigator: Shams"""
    for contact in database.select_all():
        info_box.insert(END, contact)

def delete_contact():
    selected = full_contact.get()
    cursor_selected = info_box.curselection()
    selected_phone_number = re.findall(r"\d{10}", selected) #Use a regular expression to identify the phone number from the full contact information and save it.
    database.delete_from_database(int(selected_phone_number[0]))


root = Tk() 
root.title('Contact Book') #Give our program a title
root.geometry('700x700') #Size the window
root.resizable(0, 0) #Restrict user from minimizing or resizing the window

#Create StringVar's to take inputs via entry
first_name = StringVar()
last_name = StringVar()
phone_number = StringVar()
address= StringVar()
all_elements = StringVar()

#Add labels telling users what they can enter in
Label(root, text= 'First Name').place(x=5,y=5)
Label(root, text = 'Last Name').place(x=5,y=25)
Label(root, text= 'Phone').place(x=5,y=45)
Label(root, text= 'Address').place(x=5,y=65)

#Add entry boxes and save the entry to a variable
first_name_entry = Entry(root, width=20, textvariable=first_name)
first_name_entry.place(x=80,y=5)

last_name_entry = Entry(root, width=20, textvariable=last_name)
last_name_entry.place(x=80,y=25)

phone_entry = Entry(root, width=20, textvariable=phone_number)
phone_entry.place(x=80,y=45)

address_entry = Entry(root, width=20, textvariable=address)
address_entry.place(x=80,y=65)

full_contact = Entry(root, width=30, textvariable=all_elements)
full_contact.place(x=80,y=130)

#Add buttons that will soon have commands
add_button = Button(root, text="Add", command=add_contact).place(x=20, y=90)
delete_button = Button(root, text="Delete", command=delete_contact).place(x=80, y=90,)
search_button = Button(root, text="Search").place(x=155, y=90)
view_button = Button(root, text="View All", command=view_all).place(x=235, y=90)

#Listbox that will soon store all contact information
info_box = list1 = Listbox(root, height=28, width=70)
info_box.place(x=35,y=200) 

info_box.bind('<<ListboxSelect>>', get_selected)


root.mainloop() #Keep window open until closed
