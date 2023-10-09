import sqlite3 as sql

connection = sql.connect("ContactRecordData.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE contact (ContactId INTEGER, Name TEXT, Number TEXT, Email TEXT, AddressId INTEGER)")

#cursor.execute("CREATE TABLE address (AddressId INTEGER, HouseNumber TEXT, Street TEXT, Town TEXT, Country TEXT, PostCode TEXT)")

query = """
        INSERT INTO contact
        VALUES (1,'AHMED','07424559901','ahmedscriptx@gmail.com',1000)
"""

#cursor.execute(query) 

query = """
        INSERT INTO address
        VALUES (1000,'10','DOWNING STREET','LONDON','UNITED KINGDOM','SW1A 2AA')
"""

#cursor.execute(query)

#connection.commit()

while True:

    print("""
MENU
1. Add Contact
2. Search by Name
3. Display All Contact Records And Address Records
4. Delete records
5. Modify record
6. Exit and Save Changes
          """)
    
    menuChoice = input("Enter menu choice: ")

    if menuChoice == "1":

        query = """
SELECT MAX(ContactId) FROM contact
"""

        sqlReturn = cursor.execute(query).fetchone()

        contactId = sqlReturn[0] + 1 #adding 1 to the largest contactid to get the new contactid

        query = """
SELECT MAX(AddressId) FROM address
"""

        sqlReturn = cursor.execute(query).fetchone()

        addressId = sqlReturn[0] + 1 #adding 1 to the largest contactid to get the new contactid
    
        nameInput = input("Enter name: ").upper()
        numberInput = input("Enter number: ")
        emailInput = input("Enter email :")
    
        countryInput = input("Enter country: ").upper()
        townInput = input("Enter town: ").upper()
        streetInput = input("Enter street name: ").upper()
        houseNumberInput = input("Enter house number: ")
        postCodeInput = input("Enter post code: ").upper()

        query = f"""
        INSERT INTO contact
        VALUES ({contactId},'{nameInput}','{numberInput}','{emailInput}',{addressId})
        """

        cursor.execute(query)

        query = f"""
        INSERT INTO address
        VALUES ({addressId},'{houseNumberInput}','{streetInput}','{townInput}','{countryInput}','{postCodeInput}')
        """

        cursor.execute(query)

    elif menuChoice == "2":

        nameInput = input("Enter name: ").upper()

        query = f"""
        SELECT * FROM contact
        WHERE Name = '{nameInput}'
        """

        sqlReturn = cursor.execute(query).fetchone()

        if sqlReturn:
            print(sqlReturn)

            addressId = sqlReturn[-1]

            query = f"""
            SELECT * FROM address
            WHERE AddressId = {addressId}
            """

            sqlReturn = cursor.execute(query).fetchone()

            print(sqlReturn)

    elif menuChoice == "3":

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
    elif menuChoice == "4":
        nameInput = input("Enter name to delete contact and address record: ").upper()

        query = f"""
        SELECT * FROM contact
        WHERE Name = '{nameInput}'
        """

        sqlReturn = cursor.execute(query).fetchone()
        
        if sqlReturn:

            addressId = sqlReturn[-1]

            query = f"""
            DELETE FROM contact 
            WHERE name = '{nameInput}'
            """

            cursor.execute(query)
            
            query = f"""
            DELETE FROM address 
            WHERE AddressId = '{addressId}'
            """
            
            cursor.execute(query)
    
    elif menuChoice == "5":
        full_name = input("Enter the full name of the contact: ").upper()

        print("""

        1. Change name
        2. Change number
        3. Email

        """)

        #Get the option they select

        resp = input("Select an option: ")

        #Update the full name

        if resp == '1':

                new_name = input("Enter new full name: ").upper()

                cursor.execute(f"UPDATE contact SET Name = '{new_name}' WHERE Name = '{full_name}'")

                print("Changes have been saved!")

        #Update the mobil number

        elif resp == '2':

                new_number = input("Enter new mobile phone number: ")

                cursor.execute(f"UPDATE contact SET Number = '{new_number}' WHERE Name = '{full_name}'")

                print("Changes have been made!")

        #Update the email

        elif resp == '3':

                new_email = input("Enter new email: ")

                cursor.execute(f"UPDATE contact SET Email = '{new_email}' WHERE Name = '{full_name}'")

                print("Changes have been made!")

        #Handle user error

        else:

                print("Invalid input ")

    elif menuChoice == "6":
        break

    else:

        print("\nIncorrect input, try again.")

# CustomSQL
        
#  query = """
#  DELETE FROM address
#  """

# customSQL = cursor.execute(query)


# print(customSQL)

# Commit edits, close cursor and connection
connection.commit()
cursor.close()
connection.close()
