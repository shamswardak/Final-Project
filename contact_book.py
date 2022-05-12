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
        self.conn = sqlite3.connect('contacts_database.db') #establishes connection
        self.cursor = self.conn.cursor() #establishes a cursor
        self.create_table() #creates contacts table
      
    def add_to_database(self, first_name, last_name, address, phone):
        """Function that will take in passed in first_name, last_name, address, phone and run the INSERT SQL command to add the contact into the database.
        
        Args: 
        first_name(string): first name of contact
        last_name(string): last name of contact
        address(string): address of contact
        phone(int): phone number of contact

        Returns:
        cursor.commit(): all of the contacts in the query result set
        
        Driver: Moyukh
        Navigator: Omar"""

        self.execute_with_inputs("INSERT INTO contacts VALUES (?,?,?,?)", (first_name, last_name, address, phone,)) #uses SQL code to add a contact with passed in elements
        self.commit() #commits changes
        return self.cursor.fetchall() #returns all of the contacts in the query result set
    
    def delete_from_database(self, phone):
        """Function that will delete records by phone number since every contact has a unique phone number.
        Meanwhile, values such as first names, last names, and addresses may be shared and deleting records
        by those values may unintentioanlly delete multiple records
        
        Args:
        phone(int): phone number that will be passed in to the SQL command that deletes a contact by the phone number
        
        Driver: Shams
        Navigator: Omar"""
        self.execute_with_inputs("DELETE FROM contacts WHERE phone_number=?", (phone,)) #uses SQL code to delete a contact by a passed in phone number
        self.commit() #commits changes
    
    def search_in_database(self, first_name, last_name, address, phone):
        """Function that will search for records by passed in parameters
        
        Args:
        first_name(string): first name of contact
        last_name(string): last name of contact
        address(string): address of contact
        phone(int): phone number of contact

        Returns:
        cursor.fetchall(): all of the contacts selected in the query result set
        
        Driver: Moyukh
        Navigator: Shams"""
        self.execute_with_inputs("SELECT * FROM contacts WHERE first_name=? OR last_name=? OR address=? OR phone_number=?",(first_name, last_name, address, phone,)) #uses SQL code to select a contact based on passed in search value
        self.commit() #commits changes
        return self.cursor.fetchall() #returns all of the contacts selected in the query result set
    
    def select_all(self):
        """Function that runs SQL code that selects all elements inside of contact table.

        Returns:
        cursor.fetchall(): all of the contacts in the query result set
        
        Driver: Omar
        Navigator: Shams"""
        self.execute_no_inputs("SELECT * FROM contacts") #uses SQL code to select every row from the table
        self.commit() #commits changes
        return self.cursor.fetchall() #returns all of the contacts in the query result set
    
    def create_table(self):
        self.execute_no_inputs("CREATE TABLE IF NOT EXISTS contacts (first_name TEXT, last_name TEXT, address TEXT, phone_number INTEGER)") #uses SQL code to create a table if it does not already exist

    def commit(self):
        """Function that commmits chnages to the database"""
        self.conn.commit()

    def execute_no_inputs(self, sql):
        self.cursor.execute(sql)
        self.commit()

    def execute_with_inputs(self, sql, inputs):
        self.cursor.execute(sql, inputs)
        self.commit()

def add_contact():
    """Purpose of add_contact is to get the value in each entry box and pass it into the database add_to_database function so the contact is added to the database
    
    Driver: Moyukh
    Navigator: Shams"""
    if len(first_name.get()) < 1: #if there is no first name entry, print an error and clear that entry box
        messagebox.showinfo('info', 'Please enter a first name.')
        first_name_entry.delete(0, END)
        info_box.delete(0, END)
    if len(last_name.get()) < 1: #if there is no last name entry, print an error and clear that entry box
        messagebox.showinfo('info', 'Please enter a last name.')
        last_name_entry.delete(0, END)
        info_box.delete(0, END)
    if len(phone_number.get()) != 10: #if the phone number does not have a length of 10 digits, print an error and clear that entry box
        messagebox.showinfo('Error', 'Please enter a 10-digit phone number.')
        phone_entry.delete(0, END)
    if len(address.get()) < 1: #if there is no address entry, print an error and clear that entry box
        messagebox.showinfo('info', 'Please enter an address.')
        address_entry.delete(0, END)
        info_box.delete(0, END)
    elif len(phone_number.get()) == 10 and len(first_name.get()) > 1 and len(last_name.get()) > 1 and len(address.get()) > 1: #otherwise, if all boxes are entered and valid...
        database.add_to_database(first_name.get(), last_name.get(), address.get(), phone_number.get()) #pass the entry box values into the database function to enter it into the database
        info_box.delete(0, END) #clears the listbox

        full_contact.delete(0, END) #clear the full contact box

        #clear all entry boxes
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        phone_entry.delete(0, END)
        address_entry.delete(0, END)

    for contact in database.select_all(): #for each contact in the database, add contact to the listbox
        info_box.insert(END, contact)

def get_selected(event):
    """Purpose of get selected is to get the value linked to the users cursor selection and pass it into the all_elements entry box.
    
    Driver: Shams
    Navigator: Moyukh"""
    widget = event.widget #set widget 
    index = int(widget.curselection()[0]) #get index
    content = widget.get(index) #get the content of the index
    all_elements.set(content) #set the all_elements string variable to the content

def view_all():
    """Purpose of view_all is to print all contacts from the database into the listbox
    
    Driver: Omar
    Navigator: Shams"""

    full_contact.delete(0, END) #clear the full contact box

    #clear all of the entry boxes
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)
    
    info_box.delete(0, END) #clear the listbox
    
    for contact in database.select_all(): #for each contact in the database, insert into the listbox
        info_box.insert(END, contact)

def delete_contact():
    if len (all_elements.get()) < 1: #if no contact is selected, print an error
        messagebox.showinfo('error', 'No contact selected.')
    else:
        selected = full_contact.get() #save the entire contact information
        cursor_selected = info_box.curselection() #save the cursor selected item
        selected_phone_number = re.findall(r"\d{10}", selected) #Use a regular expression to identify the phone number from the full contact information and save it.
        database.delete_from_database(int(selected_phone_number[0])) #delete the identified phone number from the database
        info_box.delete(cursor_selected) #delete the cursor selected item from the listbox
        full_contact.delete(0, END) #clear the full contact box

def search_contact():
    """Purpose of search contact is to take user inputted values and search for specific contacts using their 
    inputted values"""
    full_contact.delete(0, END) #clear the full contact box
    info_box.delete(0, END) #clear the listbox

    for data in database.search_in_database(first_name.get(), last_name.get(), address.get(), phone_number.get()): #for every result, insert it into the listbox
        info_box.insert(END, data)

if __name__ == "__main__":
    database = Database() #create Database object

    root = Tk() #create window
    root.title('Contact Book') #Give our program a title
    root.geometry('700x700') #Size the window
    root.resizable(0, 0) #Restrict user from minimizing or resizing the window

    #Create StringVar's to take inputs via entry
    first_name = StringVar()
    last_name = StringVar()
    phone_number = StringVar()
    address= StringVar()
    all_elements = StringVar()

    #Add labels telling users what they can enter in and place them
    Label(root, text= 'First Name').place(x=5,y=5)
    Label(root, text = 'Last Name').place(x=5,y=25)
    Label(root, text= 'Phone').place(x=5,y=45)
    Label(root, text= 'Address').place(x=5,y=65)

    #Add entry boxes and save the entry to a variable and place them
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

    #Add buttons that have commands (functions defined above) and place them
    add_button = Button(root, text="Add", command=add_contact).place(x=20, y=90)
    delete_button = Button(root, text="Delete", command=delete_contact).place(x=80, y=90,)
    search_button = Button(root, text="Search", command=search_contact).place(x=155, y=90)
    view_button = Button(root, text="View All", command=view_all).place(x=235, y=90)

    #Create Listbox that stores all contact information
    info_box = list1 = Listbox(root, height=28, width=70)
    info_box.place(x=35,y=200) 

    info_box.bind('<<ListboxSelect>>', get_selected) #bind the listbox to allow a cursor selection

    root.mainloop() #Keep window open until closed
