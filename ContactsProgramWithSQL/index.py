import sqlite3 as sql

connection = sql.connect("ContactRecordData.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE contact (ContactId INTEGER, Name TEXT, Number TEXT, Email TEXT, AddressId INTEGER)")

#cursor.execute("CREATE TABLE address (AddressId INTEGER, HouseNumber TEXT, Street TEXT, Town TEXT, Country TEXT, PostCode TEXT)")

query = """
        INSERT INTO contact
        VALUES (1,'Ahmed','07424559901','ahmedscriptx@gmail.com',1000)
"""

#cursor.execute(query)

query = """
        INSERT INTO address
        VALUES (1000,'10','Downing Street','London','United Kingdom','SW1A 2AA')
"""

#cursor.execute(query)

#connection.commit()

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

        contactId = sqlReturn[0] + 1 #adding 1 to the largest contactid to get the new contactid

        query = """
SELECT MAX(AddressId) FROM address
"""

        sqlReturn = cursor.execute(query).fetchone()

        addressId = sqlReturn[0] + 1 #adding 1 to the largest contactid to get the new contactid
   
        nameInput = input("Enter name: ")
        numberInput = input("Enter number: ")
        emailInput = input("Enter email :")

        countryInput = input("Enter country: ")
        townInput = input("Enter town: ")
        streetInput = input("Enter street name: ")
        houseNumberInput = input("Enter house number: ")
        postCodeInput = input("Enter post code: ")

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
        nameInput = input("Enter name: ")

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
