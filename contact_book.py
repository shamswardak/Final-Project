from tkinter import *
import sqlite3

class Database:
    """Class that will add/delete/search inside the table"""
    def __init__(self):
        """purpose of __init__() is to initialize cursor and connection to database using sqlite3"""
        self.conn = sqlite3.connect('contacts_database.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        """Purpose of create_table() is to create contacts table """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (first_name TEXT, last_name TEXT, address TEXT, phone_number TEXT)")
        self.conn.commit()
    
    def add_to_database(self, first_name, last_name, address, phone):
        self.cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", (first_name, last_name, address, phone,))
        self.conn.commit
    
    def delete_from_database(self, phone):
        """Function that will delete recordd by phone number since every contact has a unique phone number.
        Meanwhile, values such as first names, last names, and addresses may be shared and deleting records
        by those values may unintentioanlly delete multiple records
        
        Args:
        phone(int): phone number that will be passed in to the SQL command that deletes a contact by the phone number"""
        self.cursor.execute("DELETE FROM contacts WHERE phone =?", (phone,))
        self.conn.commit()
    
    def search_in_database(self, first_name, last_name, address, phone):
        """Function that will search for records by passed in parameters
        
        Args:
        first_name(string): first name of contact
        last_name(string): last name of contact
        address(string): address of contact
        phone(int): phone number of contact"""
        self.cursor.execute("SELECT * FROM contacts WHERE first_name=? OR last_name=? OR address=? OR phone=?",(first_name, last_name, address, phone,))
        self.conn.commit
    
    def select_all(self):
        self.cursor.execute("SELECT * FROM contacts")
        self.conn.commit
        return cursor.fetchall()

database = Database

class gui:
    def add_contact():
        database.add_to_database(first_name.get(), last_name.get(), address.get(), phone_number.get())


    
        

root = Tk() 
root.title('Contact Book') #Give our program a title
root.geometry('700x700') #Size the window
root.resizable(0, 0) #Restrict user from minimizing or resizing the window

#Create StringVar's to take inputs via entry
first_name = StringVar()
last_name = StringVar()
phone_number = StringVar()
address= StringVar()

#Add labels telling users what they can enter in
Label(root, text= 'First Name').place(x=5,y=5)
Label(root, text = 'Last Name').place(x=5,y=25)
Label(root, text= 'Phone').place(x=5,y=45)
Label(root, text= 'Address').place(x=5,y=65)

#Add entry boxes and save the entry to a variable
first_name_entry = Entry(root, width=20, textvariable=first_name).place(x=80,y=5)
last_name_entry = Entry(root, width=20, textvariable=last_name).place(x=80,y=25)
phone_entry = Entry(root, width=20, textvariable=phone_number).place(x=80,y=45)
address_entry = Entry(root, width=20, textvariable=address).place(x=80,y=65)

#Add buttons that will soon have commands
add_button = Button(root, text="Add").place(x=20, y=90)
delete_button = Button(root, text="Delete").place(x=80, y=90)
search_button = Button(root, text="Search").place(x=155, y=90)

#Listbox that will soon store all contact information
info_box = list1 = Listbox(root, height=28, width=70).place(x=35,y=200) 

conn = sqlite3.connect('contacts_database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contacts (first_name TEXT, last_name TEXT, address TEXT, phone_number TEXT)")

root.mainloop() #Keep window open until closed
