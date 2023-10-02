import sqlite3

connection = sqlite3.connect("aquarium.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE fish (name TEXT, Species TEXT, tank_number INTEGER)")

def insertData(): #function to let the user insert data and add it to the database
    fishName = input("Please enter name of fish: ")
    fishSpecies = input("Please enter species: ")
    tankNumber = input("Please enter tank number: ")

    cursor.execute(f"INSERT INTO fish VALUES ('{fishName}', '{fishSpecies}', {tankNumber})")
    rows=cursor.execute(f"SELECT * FROM fish").fetchall() #selecting name species and tank number from the database
    print(rows)

def searchName():
    nameToSearchFor = input("Please enter name of fish to search for: ")
    rows=cursor.execute(f"SELECT * FROM fish WHERE name = {nameToSearchFor}").fetchall() #selecting name species and tank number from the database
    print(rows)

insertData() #calling the function

searchName()


cursor.close()

