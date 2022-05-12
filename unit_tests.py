import sqlite3

#Estbalish database connection and create table for testing purposes
conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS test_contacts (first_name TEXT, last_name TEXT, address TEXT, phone_number INTEGER)")
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

        cursor.execute("INSERT INTO test_contacts VALUES (?,?,?,?)", (first_name, last_name, address, phone,))
        conn.commit()
        
        cursor.execute("SELECT * FROM test_contacts")
        conn.commit

        print(cursor.fetchall()) #using print to show us if our function is working.
    

add_to_database('John', 'Appleseed', '123 Apple Street', 11111) #running function to see if the added in contacts are listed in the database
add_to_database('Derek', 'Jones', '246 Orange Ct', 22222) #adding another one

#you may change the parameter/contact elements to add more contacts and see that the contacts are being properly passed into the SQL code

#Testing delete_from_database()
def delete_from_database(phone):
    """Function that will delete records by phone number since every contact has a unique phone number.
    Meanwhile, values such as first names, last names, and addresses may be shared and deleting records
    by those values may unintentioanlly delete multiple records
        
    Args:
    phone(int): phone number that will be passed in to the SQL command that deletes a contact by the phone number
        
    Driver: Shams
    Navigator: Omar"""
    cursor.execute("DELETE FROM test_contacts WHERE phone_number=?", (phone,)) #uses SQL code to delete a contact by a passed in phone number
    conn.commit() #commits changes

    cursor.execute("SELECT * FROM test_contacts")
    conn.commit

    print(cursor.fetchall()) #using print to show us if our function is working.
    
delete_from_database(22222) #running function to see if function deletes the contact that was inserted before.

#Testing search_in_database()
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
    cursor.execute("SELECT * FROM test_contacts WHERE first_name=? OR last_name=? OR address=? OR phone_number=?",(first_name, last_name, address, phone,)) #uses SQL code to select a contact based on passed in search value
    conn.commit() #commits changes

    print(cursor.fetchall()) #using print to show us if our function is working.
    
search_in_database('John')

#Testing select_all

def select_all():
    """Function that runs SQL code that selects all elements inside of contact table."""
    cursor.execute("SELECT * FROM test_contacts")
    conn.commit
    print(cursor.fetchall()) #using print to show us if our function is working.

select_all()

#the call to select_all() should result in the values inside of the table to return, but in this case, print.