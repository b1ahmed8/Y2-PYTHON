import sqlite3 as sql

connection = sql.connect("ContactRecordData.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE contact (ContactId INTEGER, Name TEXT, Number TEXT, Email TEXT, AddressId TEXT)")

# cursor.execute("CREATE TABLE address (AdressId INTEGER, HouseNumber INTEGER, Street TEXT, Town TEXT, Country TEXT, PostCode TEXT)")


# query = """
# INSERT INTO contact 
# VALUES (1,'Ahmed Shahzad', '07424559901', 'ahmedscriptx@gmail.com',1000)
# """
# cursor.execute(query)

# connection.commit()

while True:

    print("""
MENU
1. Add Contact
4. Display All Contact Records And Address Records
6. Exit
          """)
    
    menuChoice = input("Enter menu choice: ")

    if menuChoice == "1":

        query = """
SELECT MAX(ContactId) FROM contact
"""
        sqlReturn = cursor.execute(query).fetchone()

        addressId = sqlReturn[0] + 1 #adding 1 to the largest contactid to get the new contactid
        nameInput = input("Enter name: ")
        numberInput = input("Enter number: ")
        emailInput = input("Enter email :")


    elif menuChoice == "4":

        query = """
        SELECT * FROM contact
        """
        
        ContactRecords = cursor.execute(query).fetchall()
        print(ContactRecords)
        print("-------------------------------------")
        query = """
        SELECT * FROM address
        """        
        addressRecords = cursor.execute(query).fetchall()
        print(addressRecords)

    elif menuChoice == "6":

        break

    else:

        print("\nIncorrect input, try again.")


##CustomSQL

# query = """
#  DELETE FROM address
#  """

# customSQL = cursor.execute(query)


# print(customSQL)

##Commit edits, close cursor and connection
connection.commit()
cursor.close()
connection.close()