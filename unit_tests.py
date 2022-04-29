import sqlite3

#Estbalish database connection and create table for testing purposes
conn = sqlite3.connect('contacts_database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contacts (first_name TEXT, last_name TEXT, address TEXT, phone_number INTEGER)")
conn.commit()
    

#Testing add_to_database()
def add_to_database(first_name, last_name, address, phone):
        """Function that will take in passed in first_name, last_name, address, phone and run the INSERT SQL command to add the contact into the database.
        
        Args: 
        first_name(string): first name of contact
        last_name(string): last name of contact
        address(string): address of contact
        phone(int): phone number of contact
        
        Driver: Moyukh
        Navigator: Omar"""

        cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", (first_name, last_name, address, phone,))
        conn.commit()
        
        cursor.execute("SELECT * FROM contacts")
        conn.commit
        print(cursor.fetchall())
    

add_to_database('John', 'Appleseed', '123 Apple Street', 11111) #running function to see if the added in contacts are listed in the database

#you may change the parameter/contact elements to add more contacts and see that the contacts are being properly passed into the SQL code


